#!/usr/bin/env python3
"""Fetch Mariatta's #typooftheday posts from Mastodon.

Fetches Mariatta's Mastodon statuses tagged #typooftheday, finds which are not yet
on the blog (under content/posts/typo_of_the_day/), and creates a Hugo post
for each missing one.

Credentials are read from environment variables:

    MASTODON_INSTANCE      Default: fosstodon.org
    MASTODON_USERNAME      Default: mariatta
    MASTODON_ACCESS_TOKEN  Required. Create at <instance>/settings/applications
                           with at least the `read:statuses` scope.

Run from the repo root:

    MASTODON_ACCESS_TOKEN=... python scripts/fetch_typooftheday.py --dry-run
    MASTODON_ACCESS_TOKEN=... python scripts/fetch_typooftheday.py
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parent.parent
TYPO_DIR = REPO_ROOT / "content" / "posts" / "typo_of_the_day"
HASHTAG = "typooftheday"
SHORTCODE_RE = re.compile(
    r"\{\{\s*<\s*(?:fosstodon|mastodon)\b[^>]*\bid\s*=\s*\"(\d+)\"",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"^date:\s*(.+?)\s*$", re.MULTILINE)
TITLE_PREFIX_RE = re.compile(r"^\s*typo\s*of\s*the\s*day\s*[:\-]\s*", re.IGNORECASE)


class TextExtractor(HTMLParser):
    """Convert Mastodon's HTML status content to plain text.

    Mastodon wraps each paragraph in <p>, line breaks as <br>, and renders
    hashtags/mentions as <a> tags. We want the visible text only.
    """

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in ("br", "p"):
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "p":
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def text(self) -> str:
        return html.unescape("".join(self.parts))


def html_to_text(content: str) -> str:
    parser = TextExtractor()
    parser.feed(content)
    return parser.text()


def parse_post_date(value: str) -> datetime | None:
    """Parse a date from post frontmatter.

    Existing posts use either ISO-8601 (`2023-09-03T22:27:25.183000+00:00`)
    or RFC 2822-ish (`Wed Apr 13 17:58:53 +0000 2022`). Return an aware
    datetime, or None if neither format matches.
    """
    value = value.strip().strip('"').strip("'")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            dt = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def existing_toot_ids() -> tuple[set[str], str | None, datetime | None]:
    """Scan existing posts; return (toot ids, max toot id, latest post date)."""
    ids: set[str] = set()
    latest: datetime | None = None
    for path in TYPO_DIR.glob("*/index.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(exc)
            continue
        for match in SHORTCODE_RE.finditer(text):
            ids.add(match.group(1))
        date_match = DATE_RE.search(text)
        if date_match:
            dt = parse_post_date(date_match.group(1))
            if dt is not None and (latest is None or dt > latest):
                latest = dt
    max_id = max(ids, key=int) if ids else None
    return ids, max_id, latest


def slugify(typo_text: str) -> str:
    """Strip everything except ASCII letters and digits.

    Matches the convention of existing folders (e.g. "100% Code Cowerage" ->
    "100codecowerage", "Goofie Bag" -> "Goofiebag"). We don't normalize case
    because existing slugs aren't consistent — preserve whatever the toot used.
    """
    return re.sub(r"[^A-Za-z0-9]+", "", typo_text)


def extract_typo(plain_text: str) -> str | None:
    """Pull the typo phrase out of the toot's plain text.

    The toot must start with a "Typo of the Day:" prefix (case insensitive,
    after any leading whitespace and hashtags) — otherwise this returns None
    so the caller can skip it. Removes hashtags, strips the prefix, collapses
    whitespace. Emojis are preserved.
    """
    text = re.sub(r"#\w+", "", plain_text).strip()
    stripped = TITLE_PREFIX_RE.sub("", text, count=1)
    if stripped == text:
        return None
    stripped = re.sub(r"\s+", " ", stripped).strip()
    stripped = stripped.strip(" .—–-:")
    return stripped


def fetch_account_id(instance: str, username: str, token: str) -> str:
    url = f"https://{instance}/api/v1/accounts/lookup?{urlencode({'acct': username})}"
    req = Request(url, headers={"Authorization": f"Bearer {token}"})
    with urlopen(req) as resp:
        data = json.load(resp)
    if "id" not in data:
        raise RuntimeError(f"Account lookup failed: {data}")
    return data["id"]


def parse_link_header(header: str | None) -> dict[str, str]:
    """Parse a `Link:` header into {rel: url}."""
    if not header:
        return {}
    out: dict[str, str] = {}
    for entry in header.split(","):
        m = re.match(r'\s*<([^>]+)>\s*;\s*rel="([^"]+)"', entry)
        if m:
            out[m.group(2)] = m.group(1)
    return out


def fetch_tagged_statuses(
    instance: str,
    account_id: str,
    token: str,
    known_ids: set[str],
    min_id: str | None = None,
) -> list[dict]:
    """Fetch #typooftheday statuses newer than min_id, skipping known ids."""
    base = f"https://{instance}/api/v1/accounts/{account_id}/statuses"
    params = {"tagged": HASHTAG, "limit": "40"}
    if min_id:
        params["min_id"] = min_id
    url = f"{base}?{urlencode(params)}"
    statuses: list[dict] = []
    while url:
        req = Request(url, headers={"Authorization": f"Bearer {token}"})
        with urlopen(req) as resp:
            page = json.load(resp)
            link_header = resp.headers.get("Link")
        if not page:
            break
        hit_known = False
        for s in page:
            if s["id"] in known_ids:
                hit_known = True
                continue
            statuses.append(s)
        if hit_known:
            # Older statuses are already on the blog; no need to keep paging.
            break
        url = parse_link_header(link_header).get("next")
    return statuses


def yaml_dq(value: str) -> str:
    """Escape a string for use inside a YAML double-quoted scalar."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_post(typo: str, toot_id: str, created_at: str, instance: str) -> str:
    slug = slugify(typo)
    title = f"Typo of the Day: {typo}".rstrip()
    server_attr = "" if instance == "fosstodon.org" else f' server="{instance}"'
    return (
        "---\n"
        f"title: {yaml_dq(title)}\n"
        f"date: {created_at}\n"
        "weight: 20\n"
        "menu:\n"
        "  sidebar:\n"
        f"    name: {yaml_dq(typo)}\n"
        f"    identifier: {slug}\n"
        "    weight: 20\n"
        "    parent: typo_of_the_day\n"
        'tags: ["TypoOfTheDay"]\n'
        "type: posts/typo_of_the_day\n"
        "hero: images/posts/typo_of_the_day.jpg\n"
        "images:\n"
        "  - images/posts/typo_of_the_day.jpg\n"
        "---\n"
        "\n"
        f'{{{{<fosstodon user="mariatta"{server_attr} id="{toot_id}">}}}}\n'
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="Print actions without writing files.")
    ap.add_argument("--limit", type=int, default=None, help="Stop after N new posts (for testing).")
    args = ap.parse_args()

    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    if not token:
        print("ERROR: MASTODON_ACCESS_TOKEN is not set.", file=sys.stderr)
        return 2
    instance = os.environ.get("MASTODON_INSTANCE", "fosstodon.org").strip()
    username = os.environ.get("MASTODON_USERNAME", "mariatta").strip()

    if not TYPO_DIR.is_dir():
        print(f"ERROR: typo directory not found at {TYPO_DIR}", file=sys.stderr)
        return 2

    known, max_id, latest_date = existing_toot_ids()
    print(f"Found {len(known)} existing typo posts on the blog.")
    if max_id:
        print(f"Newest known toot id: {max_id}")
    if latest_date:
        print(f"Newest known post date: {latest_date.isoformat()}")

    print(f"Looking up @{username}@{instance} ...")
    account_id = fetch_account_id(instance, username, token)
    print(f"Account id: {account_id}")

    print(f"Fetching #{HASHTAG} statuses ...")
    statuses = fetch_tagged_statuses(instance, account_id, token, known, min_id=max_id)
    statuses.sort(key=lambda s: int(s["id"]))  # oldest first
    print(f"{len(statuses)} new toot(s) to import.")

    created = 0
    skipped: list[tuple[str, str]] = []
    to_skip = [
        '110912188875950173',
        '110058164802514883',
    ]
    for status in statuses:
        if status["id"] in to_skip:
            continue
        if args.limit is not None and created >= args.limit:
            break
        toot_id = status["id"]
        created_at = status.get("created_at", "")
        toot_dt = parse_post_date(created_at) if created_at else None
        if latest_date is not None and toot_dt is not None and toot_dt <= latest_date:
            skipped.append((toot_id, f"older than newest blog post ({created_at})"))
            continue
        plain = html_to_text(status.get("content", ""))
        typo = extract_typo(plain)
        print(f"processing {toot_id=} {typo=} ...", end="")
        if typo is None:
            text_oneline = re.sub(r"\s+", " ", plain).strip()
            skipped.append((
                toot_id,
                f"does not start with 'Typo of the day:' — full text: {text_oneline!r}",
            ))
            continue
        if not typo:
            skipped.append((toot_id, "empty after stripping prefix and hashtags"))
            continue
        slug = slugify(typo)
        print(f"{slug=}", end="")
        if not slug:
            skipped.append((toot_id, f"empty slug from typo: {typo!r}"))
            continue
        post_dir = TYPO_DIR / slug
        print(f"{post_dir=}")
        post_path = post_dir / "index.md"
        if post_path.exists():
            skipped.append((toot_id, f"file already exists: {post_path.relative_to(REPO_ROOT)}"))
            continue

        body = render_post(typo, toot_id, created_at, instance)

        rel = post_path.relative_to(REPO_ROOT)
        if args.dry_run:
            print(f"[dry-run] would create {rel}  (typo: {typo!r}, id: {toot_id})")
        else:
            post_dir.mkdir(parents=True, exist_ok=False)
            post_path.write_text(body, encoding="utf-8")
            print(f"created {rel}  (typo: {typo!r}, id: {toot_id})")
        created += 1

    print()
    print(f"Done. {created} post(s) {'would be ' if args.dry_run else ''}created. {len(skipped)} skipped.")
    for toot_id, reason in skipped:
        print(f"  skipped {toot_id}: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
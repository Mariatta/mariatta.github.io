"""Unit tests for fetch_typooftheday.py.

Run from the repo root:

    pytest scripts/
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fetch_typooftheday as mod


# ---- html_to_text ----------------------------------------------------------


@pytest.mark.parametrize(
    "html,expected",
    [
        ("<p>Hello</p>", "\nHello\n"),
        ("<p>Foo &amp; bar</p>", "\nFoo & bar\n"),
        ("Line1<br>Line2", "Line1\nLine2"),
        (
            '<p>Typo of the day: Foo <a href="x">#typooftheday</a></p>',
            "\nTypo of the day: Foo #typooftheday\n",
        ),
    ],
)
def test_html_to_text(html, expected):
    assert mod.html_to_text(html) == expected


# ---- parse_post_date -------------------------------------------------------


@pytest.mark.parametrize(
    "value,expected",
    [
        (
            "2023-09-03T22:27:25.183000+00:00",
            datetime(2023, 9, 3, 22, 27, 25, 183000, tzinfo=timezone.utc),
        ),
        (
            "2023-09-03T22:27:25Z",
            datetime(2023, 9, 3, 22, 27, 25, tzinfo=timezone.utc),
        ),
        (
            "Wed, 13 Apr 2022 17:58:53 +0000",
            datetime(2022, 4, 13, 17, 58, 53, tzinfo=timezone.utc),
        ),
        # Naive datetime is forced to UTC.
        (
            "2023-09-03T22:27:25",
            datetime(2023, 9, 3, 22, 27, 25, tzinfo=timezone.utc),
        ),
        # Surrounding quotes get stripped.
        (
            '"2023-09-03T22:27:25+00:00"',
            datetime(2023, 9, 3, 22, 27, 25, tzinfo=timezone.utc),
        ),
    ],
)
def test_parse_post_date_valid(value, expected):
    assert mod.parse_post_date(value) == expected


def test_parse_post_date_garbage_returns_none():
    assert mod.parse_post_date("not a date") is None


# ---- slugify ---------------------------------------------------------------


@pytest.mark.parametrize(
    "typo,expected",
    [
        ("100% Code Cowerage", "100CodeCowerage"),
        ("Goofie Bag", "GoofieBag"),  # case preserved
        ("", ""),
        ("!!! ???", ""),
        ("Foo \U0001f600 Bar", "FooBar"),  # emojis stripped
    ],
)
def test_slugify(typo, expected):
    assert mod.slugify(typo) == expected


# ---- extract_typo ----------------------------------------------------------


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Typo of the day: Foo Bar", "Foo Bar"),
        ("TYPO OF THE DAY: Foo", "Foo"),  # case-insensitive prefix
        ("Typo of the day - Foo", "Foo"),  # dash separator
        ("Typo of the day: Foo #typooftheday #typo", "Foo"),
        ("Typo of the day: Foo —", "Foo"),  # trailing punctuation stripped
        ("Typo of the day:   Foo    Bar", "Foo Bar"),  # whitespace collapsed
        ("Typo of the day: #typooftheday", ""),  # empty after hashtag removal
    ],
)
def test_extract_typo_match(text, expected):
    assert mod.extract_typo(text) == expected


def test_extract_typo_no_prefix_returns_none():
    assert mod.extract_typo("Just some text") is None


# ---- parse_link_header -----------------------------------------------------


def test_parse_link_header_none():
    assert mod.parse_link_header(None) == {}


def test_parse_link_header_empty():
    assert mod.parse_link_header("") == {}


def test_parse_link_header_single():
    header = '<https://example.com/next>; rel="next"'
    assert mod.parse_link_header(header) == {"next": "https://example.com/next"}


def test_parse_link_header_multiple():
    header = (
        '<https://example.com/next>; rel="next", '
        '<https://example.com/prev>; rel="prev"'
    )
    assert mod.parse_link_header(header) == {
        "next": "https://example.com/next",
        "prev": "https://example.com/prev",
    }


# ---- yaml_dq ---------------------------------------------------------------


@pytest.mark.parametrize(
    "value,expected",
    [
        ("foo", '"foo"'),
        ('has "quotes"', '"has \\"quotes\\""'),
        ("has\\back", '"has\\\\back"'),
    ],
)
def test_yaml_dq(value, expected):
    assert mod.yaml_dq(value) == expected


# ---- render_post -----------------------------------------------------------


def test_render_post_fosstodon_omits_server_attr():
    out = mod.render_post(
        "Goofie Bag", "12345", "2023-09-03T22:27:25+00:00", "fosstodon.org"
    )
    assert 'title: "Typo of the Day: Goofie Bag"' in out
    assert "date: 2023-09-03T22:27:25+00:00" in out
    assert "identifier: GoofieBag" in out
    assert 'name: "Goofie Bag"' in out
    assert '{{<fosstodon user="mariatta" id="12345">}}' in out
    assert "server=" not in out


def test_render_post_other_instance_includes_server_attr():
    out = mod.render_post(
        "Foo", "9", "2024-01-01T00:00:00+00:00", "mastodon.social"
    )
    assert 'server="mastodon.social"' in out
    assert 'id="9"' in out


def test_render_post_escapes_quotes_in_typo():
    out = mod.render_post(
        'He said "hi"', "1", "2024-01-01T00:00:00+00:00", "fosstodon.org"
    )
    assert 'title: "Typo of the Day: He said \\"hi\\""' in out


# ---- existing_toot_ids -----------------------------------------------------


@pytest.fixture
def typo_dir(tmp_path, monkeypatch):
    """Point the script's TYPO_DIR at a temp directory for the test."""
    monkeypatch.setattr(mod, "TYPO_DIR", tmp_path)
    return tmp_path


def _make_post(typo_dir: Path, slug: str, toot_id: str, date_value: str) -> None:
    d = typo_dir / slug
    d.mkdir()
    (d / "index.md").write_text(
        f"---\ndate: {date_value}\n---\n"
        f'{{{{<fosstodon user="mariatta" id="{toot_id}">}}}}\n',
        encoding="utf-8",
    )


def test_existing_toot_ids_empty_dir(typo_dir):
    ids, max_id, latest = mod.existing_toot_ids()
    assert ids == set()
    assert max_id is None
    assert latest is None


def test_existing_toot_ids_picks_largest_numerically(typo_dir):
    _make_post(typo_dir, "a", "100", "2023-01-01T00:00:00+00:00")
    _make_post(typo_dir, "b", "200", "2023-02-01T00:00:00+00:00")
    _make_post(typo_dir, "c", "150", "2023-03-01T00:00:00+00:00")
    ids, max_id, latest = mod.existing_toot_ids()
    assert ids == {"100", "200", "150"}
    assert max_id == "200"
    assert latest == datetime(2023, 3, 1, tzinfo=timezone.utc)


def test_existing_toot_ids_recognizes_mastodon_shortcode(typo_dir):
    d = typo_dir / "x"
    d.mkdir()
    (d / "index.md").write_text(
        "---\ndate: 2023-01-01T00:00:00+00:00\n---\n"
        '{{<mastodon user="someone" server="mastodon.social" id="555">}}\n',
        encoding="utf-8",
    )
    ids, max_id, _latest = mod.existing_toot_ids()
    assert ids == {"555"}
    assert max_id == "555"
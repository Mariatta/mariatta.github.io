# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio and blog for Mariatta, built with Hugo and deployed to https://mariatta.ca via GitHub Pages (gh-pages
branch), with Netlify deploy previews on PRs.

The Toha theme (v4.13.0) is still imported as a Hugo module, but **the site has been largely rewritten on top of it**.
Every page a visitor lands on is rendered by a custom layout in `layouts/`, not by Toha. Toha now supplies the `baseof`
skeleton, the top navbar partial, and asset pipeline plumbing. Its section-based homepage, its cards, and its sidebar
navigation are no longer used. Assume a page is custom-built until you've checked `layouts/`.

## Development Commands

```bash
# Install dependencies
npm install

# Local development server with live reload
hugo server -w

# Production build
hugo --gc --minify

# Update Hugo modules
hugo mod tidy
hugo mod npm pack

# Python tests (for scripts/)
pytest scripts/ -v
```

**Required toolchain:** Hugo 0.157.0 extended, Node v18.12.1, Go 1.21.

## Architecture

### Custom layouts (the actual site)

| Layout                             | Renders                   | Reads                                                            |
| ---------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| `layouts/index.html`               | `/` homepage              | recent posts + `data/en/sideprojects.yaml`                       |
| `layouts/about/list.html`          | `/about/`                 | `about`, `author`, `experiences`, `education`, `accomplishments` |
| `layouts/projects/list.html`       | `/projects/`              | `data/en/sideprojects.yaml` (grouped)                            |
| `layouts/posts/list.html`          | post/section listings     | page params (`showCount`, `countLabel`)                          |
| `layouts/_default/single.html`     | every single post         | front matter; adds fediverse meta tag                            |
| `layouts/brand/list.html`          | `/brand/` style reference | (hardcoded; `sitemap.disable: true`)                             |
| `layouts/partials/feed-entry.html` | one row in a post list    | post front matter, incl. `hero` as thumbnail                     |
| `layouts/partials/footer.html`     | footer                    | `author`, `site`                                                 |
| `layouts/partials/opengraph.html`  | OG/Twitter meta           | `defaultOgImage`, `twitterHandle`                                |

These layouts carry their **own CSS in an inline `<style>` block at the bottom of each file**. There is no shared
stylesheet for them beyond the design tokens. When you change a layout's markup, the CSS to change is in that same file.

### Design tokens

`assets/styles/override.scss` defines the runtime CSS custom properties used by every custom layout: `--c-bg`,
`--c-bg-soft`, `--c-card`, `--c-rule`, `--c-text`, `--c-muted`, `--c-faint`, `--c-rose`, `--c-rose-soft`,
`--c-rose-tint`, `--font-sans`, `--font-mono`. Light values on `:root`, dark values on `html[data-theme='dark']`.

**Never hardcode a color or font family in a layout.** Use the tokens, so dark mode keeps working. `/brand/` is a live
reference page for the system. Typefaces are IBM Plex Sans and IBM Plex Mono.

### Data files (`data/en/`)

Live, and rendered somewhere:

- `author.yaml` — name, image, contact info, and the `summary` list of role one-liners shown on `/about/`
- `site.yaml` — copyright, site description, OpenGraph defaults, `customMenus` (the top navbar links)
- `sideprojects.yaml` — **single source of truth** for both the homepage "Other projects" section and `/projects/`
- `sections/about.yaml` — the `/about/` summary prose and the "Elsewhere" social links
- `sections/experiences.yaml`, `sections/education.yaml` — the Experience and Education blocks on `/about/`
- `sections/accomplishments.yaml` — the Recognition block on `/about/`; supports `certificateURL` (links a PDF in
  `static/files/`) and an optional `badge: {image, alt}` for an award logo

Leftovers from the Toha era that **no layout reads**. Editing these changes nothing on the site:

- `sections/achievements.yaml`, `sections/projects.yaml`, `sections/publications.yaml`, `sections/recent-posts.yaml`

### Content

`content/posts/` holds everything, organized by type: `talks/`, `ice_cream_selfies/YEAR/`, `typo_of_the_day/`,
`speaker_bio/`, and top-level blog posts. `content/about/`, `content/projects/`, and `content/brand/` are stub
`_index.md` files that exist to give their custom layouts a page to attach to; the content lives in the layout or in
`data/`.

### Static assets

- `assets/images/` — Hugo-processed images. Site chrome (logo, favicon, backgrounds) lives in `assets/images/site/` and
  is what `config.yaml`'s `logo:`/`background:` paths resolve to, despite those paths reading like `/images/...`.
- `static/images/` — copied verbatim to `/images/...`. Use it for images referenced directly from a layout or a data
  file, where you want a stable URL and no processing.
- `static/files/` — PDFs (award certificates) served at `/files/...`

Both directories end up under `/images/` in the built site, so check `assets/images/` first when a path looks missing.
Post images generally live inside the post's own page bundle directory.

## Creating Content

```bash
# New blog post
hugo new posts/my-post-name/index.md

# New ice cream selfie post
hugo new --kind ice_cream_selfies posts/ice_cream_selfies/YEAR/event-name/index.md

# New talk post
hugo new --kind talks posts/talks/YEAR/talk-name/index.md
```

### Post front matter

YAML front matter. What the custom layouts actually read:

- `title`, `date`, `draft`, `description` (used as the list excerpt and meta description)
- `tags` — array of strings; rendered as links to `/tags/<tag>/`
- `hero` — path to a hero image; doubles as the thumbnail in post lists and the OG image fallback
- `images` — array for Open Graph
- `subtitle` — optional, rendered under the title

The archetypes still emit `menu.sidebar` blocks. Toha's sidebar nav is no longer rendered, so those are inert; harmless
to leave, safe to omit in new posts.

Raw HTML is allowed in markdown (`markup.goldmark.renderer.unsafe: true`).

### Shortcodes

- `{{< fosstodon user="mariatta" id="..." >}}` — embeds a Mastodon post (custom, `layouts/shortcodes/`)
- `{{< gallery match="images/foo/*" ... >}}` — image gallery, from the `hugo-shortcode-gallery` module
- `{{< img src="..." align="center" title="..." >}}` — from Toha

## Automation

- `scripts/fetch_typooftheday.py` — fetches `#typooftheday` posts from Mastodon and writes new Hugo posts under
  `content/posts/typo_of_the_day/`. Needs `MASTODON_ACCESS_TOKEN`. Supports `--dry-run`.
- `scripts/test_fetch_typooftheday.py` — pytest suite for the above; runs in CI on every PR.

## CI/CD

- `.github/workflows/deploy-site.yaml` — on push to `main`, builds and publishes to the `gh-pages` branch with the
  `mariatta.ca` CNAME
- `.github/workflows/tests.yaml` — runs `pytest scripts/` on PRs and pushes to `main`
- `.github/workflows/typo-of-the-day.yaml` — daily at 15:00 UTC, runs the Mastodon import script and opens a PR
- **Netlify** — deploy previews for PRs (`netlify.toml`); production build is `hugo --gc --minify`
- **pre-commit** — prettier formats markdown, wrapping prose at 120 chars (see `.prettierrc.yaml`)

## Privacy posture

This is deliberate; don't undo it while "modernizing" something:

- Disqus comments and Google Analytics have been **removed**, and are additionally hard-disabled under `privacy:` in
  `config.yaml` as a backstop
- YouTube embeds go through youtube-nocookie.com; DNT is enabled for X and Vimeo
- No third-party trackers, no cookie banner

## Gotchas

- The `categories` taxonomy is deliberately removed from `config.yaml`. Re-adding it makes Hugo generate an empty
  `/categories/` page, which hits a bug in Toha v4.13.0 (its `categories/list.html` calls a pagination partial the theme
  doesn't ship) and breaks the build.
- Stage specific paths. `git add -A` in this repo sweeps in build output and PDFs you may not have meant to publish.
  Everything under `static/files/` becomes a public URL the moment it merges.
- Toha's navbar renders a sidebar-toggle button, but no custom layout defines a sidebar block, so the button does
  nothing. Not worth chasing unless you're touching the navbar.

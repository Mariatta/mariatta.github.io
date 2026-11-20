---
title: "Gidgethub Is in Maintenance-Only Mode"
subtitle: "And v6.0.1 is out, to say so more clearly"
date: 2026-11-20T09:00:00-08:00
draft: false
description:
  "Since v6.0.0, gidgethub has been in maintenance-only mode: bug reports are welcome, feature requests and external
  pull requests are not. We said so on social media and not much louder. v6.0.1 fixes that."
tags: ["gidgethub", "Open Source", "Python", "Maintainership"]
images:
  - /posts/gidgethub-maintenance-only/gidgethub-maintenance-only.jpg
hero: /posts/gidgethub-maintenance-only/gidgethub-maintenance-only.jpg
---

If you use [gidgethub](https://github.com/gidgethub/gidgethub), here's some news you may have missed: as of v6.0.0,
released on September 25, 2026, the project is in **maintenance-only mode**.

What that means in practice:

- **Bug reports are welcome.** We'll make a best-effort attempt at fixing them.
- **Feature requests are not accepted**, and will be closed.
- **Pull requests from external contributors are not accepted.** PRs are disabled on the repository.

It still works, it still gets bug fixes, and v6.0.0 was a big release. It just isn't growing anymore.

The CPython core workflow bots still run on it: [bedevere](https://github.com/python/bedevere),
[blurb-it](https://github.com/python/blurb_it), and [miss-islington](https://github.com/python/miss-islington).

## How we decided

It was a short conversation, and it happened on Labour Day.

Brett had been taking stock of the open source projects that take up his time without giving much back, and gidgethub
was one of them. He asked whether I wanted to keep it going, or wind it down instead: close it to outside contributors,
work through what was still open, and eventually archive it.

I was already feeling the same way. I haven't been building anything with gidgethub, so I didn't feel like a good judge
of which new features it should have. We settled on doing what the [requests](https://github.com/psf/requests) library
does and not taking feature requests, with Brett and me as the only ones sending PRs for fixes. A thumbs up from me, and
that was the whole decision.

## Why you're hearing about it now

Brett and I didn't keep this a secret, but we didn't exactly shout it either. Brett
[posted about it on Mastodon](https://mastodon.social/@brettcannon/117271883257045196):

> On Labour Day, @mariatta and I decided to put Gidgethub into maintenance mode; we will accept bug reports but no
> feature requests, PRs only by us.
>
> As such, I spent the weekend closing out all remaining issues-- both bug reports and feature requests --in hopes that
> the project is in a good state to just work and do what people need going forward. I'll let the code settle before a
> doing 6.0 release.
>
> And if people need more, they can fork.

Then 6.0.0 came out. Besides that post, the contributing guide said so, and the README mentioned it several sections
down. That was about it.

[C.A.M. Gerlach](https://github.com/CAM-Gerlach) pointed out in
[issue #255](https://github.com/gidgethub/gidgethub/issues/255) that this wasn't enough. He only found out because
[Hugo](https://github.com/hugovk) mentioned it in passing on
[cherry-picker#192](https://github.com/python/cherry-picker/issues/192). It wasn't in the docs, it wasn't in the
changelog, and there was no issue template to catch anyone before they filed a feature request.

He was right. Part of me underestimated how much this kind of news matters to the people who depend on the library. If
you're choosing a GitHub API library for a new project, whether it's still accepting features is exactly the kind of
thing you'd want to know up front, not after you've opened an issue asking for one.

So consider this the official announcement, for everyone who missed the casual one.

## gidgethub v6.0.1

[v6.0.1](https://github.com/gidgethub/gidgethub/releases/tag/v6.0.1) came out yesterday. It makes the status hard to
miss:

- A maintenance-only notice at the top of the README and the [docs](https://gidgethub.readthedocs.io/), plus a status
  badge.
- A [changelog entry](https://gidgethub.readthedocs.io/en/latest/changelog.html) recording that this has been the case
  since 6.0.0.
- An issue template that says so before you start typing, with blank issues turned off.

v6.0.1 is a documentation-only change.

## What's in 6.0.0, if you skipped it

Since 6.0.0 is the release that went quietly into maintenance mode, its changes are worth a mention too. The highlights:

- Managed GitHub App authentication: pass `app_id` and `private_key` to `GitHubAPI`, and JWTs are generated, cached, and
  refreshed for you. ([#252](https://github.com/gidgethub/gidgethub/pull/252))
- New `manage_rate_limit()` and `handle_rate_limit_error()` hooks, so you can plug in your own rate-limit and retry
  strategy. ([#19](https://github.com/gidgethub/gidgethub/issues/19))
- 422 responses with string `errors` now raise `ValidationError` instead of `TypeError`.
  ([#250](https://github.com/gidgethub/gidgethub/pull/250))
- Python 3.10 is the new minimum. ([#248](https://github.com/gidgethub/gidgethub/pull/248))

The full list is in the [6.0.0 changelog](https://gidgethub.readthedocs.io/en/latest/changelog.html).

Thanks to C.A.M. Gerlach for bringing this to our attention, and for doing it kindly. This post exists because of that
issue.

And thank you to everyone who has used gidgethub, filed issues, and contributed over the years. Your bug reports, PRs,
and bots built on top of it are what made it worth maintaining.

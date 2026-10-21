---
title: "Python Core Sprint 2026: Day 2"
slug: "python-core-sprint-2026-day-2"
date: 2026-10-21T07:00:00-07:00
description:
  "Day 2 of the Python Core Sprint 2026. Flipping bedevere, blurb_it, and miss-islington from Heroku to the PSF's
  Cabotage, one bot at a time, and the parts that did not go as smoothly as it looked from the outside."
draft: false
menu:
  sidebar:
    name: "Python Core Sprint 2026: Day 2"
    identifier: python-core-sprint-2026-day-2
    parent: posts
images:
  - /posts/python-core-sprint-2026-day-2/python-core-sprint-2026-day-2.png
hero: /posts/python-core-sprint-2026-day-2/python-core-sprint-2026-day-2.png
tags:
  - Python
  - Open Source
  - Sprint
  - Core Dev
  - Infrastructure
  - Bots
  - GitHub
  - Learnings
---

Day 2 of the [Python Core Sprint](/posts/python-core-sprint-2026-day-1/) was all about one thing for me: moving our
GitHub bots, [bedevere](https://github.com/python/bedevere), [blurb_it](https://github.com/python/blurb_it), and
[miss-islington](https://github.com/python/miss-islington), off Heroku and onto the PSF's
[Cabotage](https://github.com/cabotage/cabotage-app). Monday was prep. Yesterday was the switch.

The facts first. The downtime was announced for 11 AM to 12 noon Pacific. Here is how it went, in Pacific time:

- **11:00 AM**: posted on Discord that the downtime was starting.
- **11:35 AM**: bedevere switched over to Cabotage.
- **11:58 AM**: blurb_it switched over, and bedevere #717 merged to point at it.
- **12:08 PM**: miss-islington switched over.
- **12:17 PM**: first backport created on Cabotage.
- **12:36 PM**: updated the [Discourse thread](https://discuss.python.org/t/planned-downtime-for-our-github-bots/109556)
  to say "This is now completed."

Zachary Ware commented that it sounded like it went very smoothly.

Yes, I think so. Honestly, I did not know what to expect going in. I was imagining we would lose some webhook events,
that a few PRs would miss their labels or their backports, and that I would spend the afternoon redelivering things.
None of that happened. Nobody lost a PR, nobody lost a backport, and as far as I can tell nobody noticed much at all. It
helps a lot that Heroku and Cabotage are so compatible: the same Procfile, the same environment variables, the same
twelve-factor shape of app. The bots did not have to change much to move.

On Monday Guido joked that I had picked the one week everyone is pushing code to take down the infrastructure. So at 11
AM: time to take down the infrastructure. Except nothing was really down. In hindsight, that is the sign of great
infrastructure. After all, Cabotage is the same platform that powers [PyPI](https://pypi.org/), which is a much bigger
deal, at a much larger scale, than three bots.

From the inside, it was a lot of little tidbits. A lot of screens to look at. A lot of buttons on different Cabotage
pages that need to be clicked in a particular order at particular times, with a GitHub settings page open in the next
tab, the process logs in another, and Sentry and the GitHub App's recent deliveries page in two more. None of it was
hard. All of it needed attention. So this post is the story of what the switch actually involved, bot by bot, including
the one part that did not go well, which is at the end.

### Waking up to a security alert

Yesterday I woke up to a notification on my phone: two GitHub security advisories for
[aiohttp](https://docs.aiohttp.org/), the web framework all three bots are built on. One for
[a missing initial request timeout](https://github.com/advisories/GHSA-5wr8-gcqf-gqf3), one for
[unbounded memory and CPU use on crafted requests](https://github.com/advisories/GHSA-2g87-pp6c-29x5), both rated high,
both fixed in `aiohttp` 3.14.4. Not what I wanted to see on the day I was about to rebuild and redeploy all three bots.

But by the time I got up, the team had already acted on it. The advisories had gone out the day before, Dependabot had
opened the `aiohttp` bump in each repo, and other core devs had merged them: Ezio Melotti in
[miss-islington](https://github.com/python/miss-islington/pull/747) overnight, Stan in
[blurb_it](https://github.com/python/blurb_it/pull/468) and Jelle Zijlstra in
[bedevere](https://github.com/python/bedevere/pull/716) first thing in the morning. So the images I built for Cabotage
later in the day already had the fix in them. Thanks to them for keeping on top of things.

### Holding the backport for a security release

At 11 AM I posted on the core dev Discord that I was starting the downtime now. Soon after, Thomas Wouters asked if we
could hold off a little:

> I'm not sure which bots would be affected but it would be nice to get backports of the pip update we need to do
> ([python/cpython#159910](https://github.com/python/cpython/pull/159910))

The pip update was needed for a security release, and the release team wanted it merged and backported to the release
branches before the backport bot went anywhere. That is exactly the kind of thing the downtime notice was for. The bot
that does backports is miss-islington, so I said I could do miss-islington last, and started with bedevere. By the time
I was done with bedevere, Thomas said they were done too: the pip PR had merged at 11:46 and miss-islington on Heroku
had created its backports.

### How each bot is different

All three bots are small `aiohttp` apps that receive GitHub webhooks. That is where the similarity ends, and the order
in which I flipped them follows how much state each one carries. I'm writing the steps out below the way I'd want them
in a runbook, because next time it will be someone else doing this, or me again having forgotten all of it. As I joked
on the core devs Discord channel: "I'm not an agent. My context expired."

This is the flip day section of the checklist in Television, as it looked by the end of the day:

{{<img src="/posts/python-core-sprint-2026-day-2/images/tv/tv-flip-day-checklist.png" title="The flip day section of the migration checklist in Television, everything ticked" width="640">}}

#### bedevere: just webhooks

bedevere is the most straightforward. It is stateless: a webhook comes in, bedevere looks at the PR, and it comments,
labels, or sets a status check. There is nothing to clone, nothing to store, and no login.

Before the flip:

- In Cabotage, open the bedevere application and check that it has a public ingress. Cabotage only creates one
  automatically when an application is first created, and the bedevere app predates that feature, so it had none. I
  created it by hand on the Ingress page. Name it after the process, `web`. My first attempt, named `bedevere`, got a
  hostname that never received a real certificate and served a 404.
- Open `https://<ingress hostname>/health` in the browser and check for a 200 with a valid certificate.
- Check that the application has a GitHub App set up in its Cabotage settings, otherwise Cabotage is never told about
  new commits and will not rebuild on merge to `main`. bedevere had none. Setting it up needed permissions I do not
  have, so I asked Jacob to do it. This is exactly the kind of thing I meant on day 1 about having him in the same room.
  Heroku, meanwhile, kept happily auto-deploying `main` to the app I was about to turn off.
- Build from `main`, create a release, deploy, and scale `web` to 1. Leave it idling and check the process log.

The flip:

- Go to the python organization settings on GitHub, then Developer settings, then GitHub Apps, then `bedevere-app`.
- Change the Webhook URL from the Heroku hostname to the Cabotage ingress hostname. Save.
- Watch the Cabotage web log for the first delivery, and the GitHub App's Advanced tab, which lists recent deliveries
  with their response codes.
- Rollback is the same field with the Heroku hostname in it.

I flipped it at 11:35:56 and watched the first successful delivery come in on the Cabotage web log. That timestamp is
the one I put on the Discourse thread.

After the switch, I noticed we still had the old webhooks around, the ones configured directly on the repository from
before the bots became GitHub Apps. I did that migration at the core sprint in Brno, three years ago, and these hooks
had been sitting there inactive ever since. Once I had confirmed the switch to Cabotage was working, I deleted them.

#### blurb_it: a UI, so an order of operations

[blurb_it](https://blurb-it.python.org/) is the one with a user interface. Contributors log in with GitHub and add a
news entry to their PR from the browser. That means it has an OAuth callback URL, which has to match the hostname the
app thinks it is running on, which has to match what bedevere links to when it tells a contributor their PR is missing a
news entry. So blurb_it's switch is changes in several places, and they have to land close together.

Before the flip:

- Decide the public hostname. The auto-generated Cabotage hostname is a mouthful, something like
  `python-blurb-it-blurb-it-c1b03c35-web.psfhosted.net`. Creating a hostname under `python.org` is not something I can
  do, or decide on, so I kept that URL and opened the bedevere PR pointing at it. Stan
  [asked on the review](https://github.com/python/bedevere/pull/717#discussion_r4328508543) for "a less scary domain",
  since this is a site contributors sign in to with their GitHub account, and the obscure hostname looked dodgy. Fair.
  Jacob, who can decide that, set up `blurb-it.python.org` right there in the review thread: a CNAME to the ingress, a
  second hostname on the Cabotage ingress, and a Let's Encrypt certificate.
- In Cabotage, check the application settings. Two fields were wrong for blurb_it and are easy to miss: the health check
  path was the Cabotage default with a trailing slash, while the app serves `/health` without one, and deploys only
  passed because the error middleware answered 200 for any unknown path, which
  [#465](https://github.com/python/blurb_it/pull/465) was about to fix. And the auto-deploy branch was empty, so merges
  to `main` would not have deployed at all. Set the health check path to `/health` and the auto-deploy branch to `main`.
- Have the bedevere change ready. bedevere's `news.py` had the blurb_it URL hardcoded, so
  [bedevere #717](https://github.com/python/bedevere/pull/717) has to merge at the same time as the flip, otherwise
  bedevere keeps pointing contributors at the Heroku app.

The flip, in this order:

- On the `blurb-it` GitHub App settings page, update the homepage URL, the setup URL, the callback URL, and the webhook
  URL from `blurb-it.herokuapp.com` to `blurb-it.python.org`. There is a single callback URL, so replacing it means
  signing in on the Heroku app stops working at that moment. Rollback now needs the Heroku callback re-added.
- In Cabotage, set `APP_URL` to `blurb-it.python.org`. The app uses it to build the sign-in redirect and the how-to
  link. Create a release and deploy it.
- Merge bedevere #717.
- Open the site, sign in with GitHub, and add a blurb to a test PR.

#### miss-islington: a worker, and the riskiest one

miss-islington is the backport bot, and it is the one I was most worried about. Unlike the other two, it is not just a
web process. It has a Celery worker, which talks to Redis, and which keeps a full clone of CPython on disk so that it
can cherry-pick merged commits onto the release branches. The clone happens when the worker starts, not lazily, and
cherry-picking needs history, so no shallow clone.

Before the flip:

- Check which commit the live release was built from. On Monday night the live miss-islington release on Cabotage was
  still built from Jacob's February commit, not from the merged `main` with the fixes in it. Cabotage's Deploy button
  only re-releases the latest image it already has. A new commit needs three separate steps on three separate pages:
  Images, Build from Source; then Create Release; then Deploy. If you only press Deploy, you get the old code with a new
  release number, and nothing in the UI shouts about it.
- Give the worker enough resources. The default pod class was not enough for a full CPython clone, so the `worker`
  process had to be moved to a larger pod size. Even then the clone takes about two minutes every time the pod starts,
  because the disk is ephemeral.
- Scale `web` to 1 and `worker` to 1, then watch the worker log for three things in order: the clone finishing,
  `Connected to rediss://...`, which confirms the Redis connection is verified against Cabotage's certificate authority
  and not the Heroku-era "don't check the certificate" override, and then the ready line.

The flip:

- On the `Miss Islington App` GitHub App settings page, change the Webhook URL to the Cabotage ingress hostname.
- Watch the web log for GitHub's deliveries getting 200s, which means signature validation worked.
- Then test for real. A healthy webhook is not a backport, and there is no way to test a backport bot other than merging
  something with a backport label on it.

I flipped it at 12:08, saw the 200s, and at 12:12 posted in the core dev Discord:

> Miss islington is rolled over as well. webhook events look healthy. Does anyone wanna merge a PR and backport? 😀

Stan took me up on it. His [python/cpython#159566](https://github.com/python/cpython/pull/159566) got merged with
backport labels, and at 12:17 miss-islington on Cabotage replied "I'm working now to backport this PR to: 3.15" and
"3.14", and two backport PRs appeared a few seconds later. By 12:28, three merged PRs had produced six backport PRs, and
two of those were already merged. I posted the link back to Discord as the first successful backport on Cabotage, and
updated the Discourse thread.

### The datetime docs PR, finally merged

One of those three merged PRs was mine. The [datetime docs PR](https://github.com/python/cpython/pull/125009) I wrote
about in the day 1 post, the one that had been open for two years, got its last approval, and I merged it at 12:23, in
the middle of watching the new backport bot. It was the third PR miss-islington backported on Cabotage, to 3.14 and
3.15, and both backports were merged about an hour later. A small change that took two years to land, and it got to be
part of the first batch of backports on the new platform.

### The part that did not go well: a token in the logs

When the miss-islington worker first started on Cabotage, before the `nobody` user fix was fully right, the CPython
clone failed a few times. miss-islington authenticates its git operations with a personal access token in the `GH_AUTH`
environment variable, and the code embedded that token directly in the clone URL. When `git clone` fails, Python's
`CalledProcessError` traceback prints the full command line it ran. Token included. In plaintext. Into the Cabotage
process logs.

The logs are only visible to people with access to the miss-islington application on Cabotage. That is eight people: PSF
staff, other core developers who maintain other apps on Cabotage like the buildbot, and me. All of them trustworthy, and
none of them a stranger. So this was not a public leak. It was still a leak, and the right response to a credential in a
log is to rotate it, not to delete the log line. So I rotated the token and released the new one as a config-only
release.

Then I fixed the cause. [miss-islington #749](https://github.com/python/miss-islington/pull/749) supplies the token
through a git credential helper that reads `GH_AUTH` from the environment only when git asks for it. The clone URL and
the remote URL are plain, so the token no longer appears in command lines, in `.git/config`, or in tracebacks. It also
adds a test that runs the repository setup with a sentinel token and asserts it is absent from every git command.

And then it leaked a second time. When I deployed the fix, the rollout interrupted an old-code pod in the middle of its
clone, the old code's traceback printed its argv one last time, and the freshly rotated token went into the log too. So
I rotated it again, after the new code was confirmed live. Both tokens that ever appeared in a log are now dead.

The longer-term fix, which Sviatoslav
[suggested on the original Cabotage support PR](https://github.com/python/miss-islington/pull/729#discussion_r2987962719),
is to stop using a long-lived personal token at all and have miss-islington push with short-lived GitHub App
installation tokens, the way patchback does. That is on the follow-up list.

I could have left this part out of the post. I'm including it because I want to be transparent about it, and because I
think it is a useful lesson for people like me, who build web apps without being security experts: a token in a URL is a
token in every error message that URL ever appears in. Keep credentials out of command lines, and when one does end up
in a log, rotate it, even if you trust everyone who could have read it.

### Watching, then turning off Heroku

The plan from Monday was to watch for a few hours before touching Heroku, and that is what I did. The GitHub App recent
deliveries pages for all three apps showed nothing but 200s. Sentry was quiet. Backports kept flowing through the
afternoon and evening. At 2:27 PM I scaled all three Heroku apps to zero dynos and put them in maintenance mode, and
verified it with `heroku ps` and `heroku maintenance`.

That changes what rollback means. Until that moment, rolling back was flipping a URL. Now it is scaling Heroku back up,
turning maintenance off, and then flipping the URL, plus re-adding the Heroku callback on the blurb_it GitHub App. I'm
comfortable with that. The apps themselves and the Heroku Redis add-on stay around until a few quiet days have passed,
and then they get deleted.

With the bots on Cabotage, the rest of the day went into the follow-ups from the tracker:

- A Docker build job in CI for all three repos ([bedevere #718](https://github.com/python/bedevere/pull/718),
  [blurb_it #471](https://github.com/python/blurb_it/pull/471),
  [miss-islington #750](https://github.com/python/miss-islington/pull/750)), so that a broken Dockerfile fails in CI
  instead of at deploy time. All three merged late in the afternoon.
- [miss-islington #751](https://github.com/python/miss-islington/pull/751) removes the Heroku leftovers: `runtime.txt`,
  the Heroku Redis fallback, the `CERT_NONE` SSL settings, and bumps the image to Python 3.15, which Hugo asked for.
- A Python and dependency round for all three bots, since they were still building on Python 3.11. The bots are deployed
  apps running on one interpreter, so I'm keeping the CI matrix to the version in the Dockerfile plus the previous one
  as a fallback, and dropping versions that are security-only.
- The contributing docs for bedevere now describe Cabotage instead of Heroku
  ([#714](https://github.com/python/bedevere/pull/714)).

By the end of the day the [Television](https://television.run/) board for the project had every migration task ticked,
including "Heroku scaled to zero", and the checklist had grown a new section of pull requests in the three repos that
need a review or a decision, some of them from 2018.

{{<img src="/posts/python-core-sprint-2026-day-2/images/tv/tv-cpython-bots-board.png" title="The CPython bots project board in Television the morning after: every migration phase done, 19 follow-up tasks open" width="640">}}

### The rest of the sprint

There were presentations and breakout sessions throughout the day, which I mostly skipped. I had committed to the
downtime, publicly and with a time on it, so I wanted to follow through and prioritize that over everything else
happening in the room.

After the sprint day there was a happy hour. I stayed for a bit, then had to leave early.

---
title: "Python Core Sprint 2026: Day 1"
slug: "python-core-sprint-2026-day-1"
date: 2026-10-20T07:00:00-07:00
description:
  "Day 1 of the Python Core Sprint 2026. Reviving a two-year-old datetime docs PR, and announcing a planned downtime for
  our GitHub bots as they move from Heroku to the PSF's Cabotage."
draft: false
menu:
  sidebar:
    name: "Python Core Sprint 2026: Day 1"
    identifier: python-core-sprint-2026-day-1
    parent: posts
images:
  - /posts/python-core-sprint-2026-day-1/python-core-sprint-2026-day-1.jpg
hero: /posts/python-core-sprint-2026-day-1/python-core-sprint-2026-day-1.jpg
tags:
  - Python
  - Open Source
  - Sprint
  - Core Dev
---

This week I'm in San Francisco for the annual Python Core Sprint. This year the sprint is hosted by Brandt Bucher from
OpenAI, at OpenAI's office, and runs Monday to Friday, October 19 to 23. I'm only here for the first three days. On
Thursday I fly out to Seattle for [SeaGL](https://seagl.org/), where I'm one of the keynote speakers :)

I could not make it to last year's sprint at Arm in Cambridge, UK, and it is unlikely I'll be able to make it to next
year's European sprint either, so I'm glad this one is on the West Coast and within reach. The sprint is one of the very
few times in a year when this many Python core team members are in the same room, focused on nothing but Python. It is
still one of my favorite Python events of the year. Thank you to Brandt and OpenAI for hosting us!

I'm here thanks to a travel grant from the PSF, which covers my lodging and airfare. Thank you, PSF!

Here is what I did and worked on yesterday, on day 1 of the sprint, starting from the night before.

### Pre-sprint dinner

{{<img src="/posts/python-core-sprint-2026-day-1/images/dinner/presprintdinner.jpg" title="Pre-sprint dinner" width="640">}}

A few of us are staying in the same hotel, so on Sunday night six of us went out for dinner together: Barry Warsaw, Hood
Chatham, Jacob Coffee, Diego Russo, Mark Shannon, and me. The meal was nice, and it was nice catching up. I ordered a
fun-sounding appetizer called Happy Spoon, which lived up to its name.

{{<img src="/posts/python-core-sprint-2026-day-1/images/dinner/happyspoon.jpg" title="Happy Spoon appetizer" width="320">}}

#### Then the bill arrived

The waitstaff told us they could only split the bill two ways, not six. Can't, or won't? This is simply not a thing in
Canada. Back home, the waitstaff would happily split the bill however many ways we'd like. Six people, six bills, each
person pays for what they ordered, and nobody has to do arithmetic at the table. It is so normal that it did not occur
to me to ask about it ahead of time.

So we got into the discussion of who pays, and how much, and who owes whom. Someone said "just Venmo me", which I
couldn't: Venmo is not available outside of the USA. I went to an ATM on Monday to pay them back in cash. The restaurant
also did not tell us ahead of time that they could not split the bill, which is a problem on its own. I vented about it
on Mastodon, and apparently this is extremely common in the US, and basically nowhere else.

{{<fosstodon user="mariatta" id="117465950278767281">}}

As a developer, I know this is not a technical limitation. A point-of-sale system is perfectly capable of splitting a
bill many ways, or by item. Systems that do it exist, and the rest of the world uses them. So I put this on the business
for choosing a system that cannot do it, or for choosing not to use the feature. What bothers me most is the assumption
baked into that choice: someone decided that two ways is enough, that a larger group is an edge case, and everyone went
along with it. But a group of friends or colleagues going out together is not an edge case. It is the most common way
people eat out.

{{<fosstodon user="mariatta" id="117466060455695132">}}

I already have an expense splitting app on [Secret Codes](https://github.com/Mariatta/secretcodes), which I built based
on my past experiences traveling with friends and family. After that dinner, I decided to update it. Until Sunday night
it could only split an expense equally between everyone. Now
([the PR](https://github.com/Mariatta/secretcodes/pull/163)) I can create an event, add the people at the table, enter
several expenses at once, and split each one by item, so whoever ends up paying the whole bill can see precisely who
owes what. Next time I'll ask about splitting before we sit down.

{{<fosstodon user="mariatta" id="117468111339562778">}}

### Reviving a datetime docs PR

I started the day with something small, to warm up. Right after my last core sprint, at Meta in 2024, I opened
[a docs PR](https://github.com/python/cpython/pull/125009) for
[gh-124549](https://github.com/python/cpython/issues/124549), which is about `datetime.strptime` quietly accepting an
over-specified format string. If the format contains more than one directive for the same field, for example both `%Y`
and `%y`, every directive still has to match the input, but only the value from the last one gets used:

```python
>>> datetime.strptime("200099", "%Y%y")
datetime.datetime(1999, 1, 1, 0, 0)
```

The PR just adds a note in the `datetime` docs explaining this behaviour. A handful of lines. So why has it been open
for two years?

Because the question of _where_ the note goes turned out not to be simple, and we ended up discussing it several times
at the [Python Docs Editorial Board](https://python.github.io/editorial-board/). The `datetime` reference is one of the
ten largest files in the whole documentation. It is long enough that the page opens with a "skip to the format codes"
link, and the format code table already carries a long list of numbered footnotes underneath it. My note originally went
in as yet another footnote on that table. The first review question was, reasonably, "is a note here the best place for
this?" And there was no good answer, because the real fix is to restructure the page, not to make the footnotes longer.

The board's position, written up in the
[April 14 meeting notes](https://python.github.io/editorial-board/updates/2026-04-14/), is that `datetime.rst` should be
split up, starting by moving the format codes onto their own page. Splitting a page needs redirects so that the old
anchors keep working, and the redirect mechanism for the docs is still being worked out, which has been holding up other
docs work too. In the meantime the board asked that the two behavioural notes in my PR become proper standalone
directives near the format codes, rather than footnotes buried in the table, so that they survive the eventual split
intact. Stan has a [follow-up PR](https://github.com/python/cpython/pull/132524) for the code side of the same issue,
which makes `strptime` warn when directives conflict.

So yesterday I fast-forwarded the PR to the latest `main` and reorganized it the way the board asked. Stan already left
a suggestion with tighter wording. Hopefully this one finally lands this week.

I'm telling this story to show that in Python, even a small change is not that simple to make.

### Announcing downtime for our GitHub bots

The bigger project for me this week is migrating our GitHub bots, [bedevere](https://github.com/python/bedevere),
[miss-islington](https://github.com/python/miss-islington), and [blurb-it](https://github.com/python/blurb_it), from
Heroku to the PSF's [Cabotage](https://github.com/cabotage/cabotage-app). These bots do a lot of the invisible work on
the CPython repository: checking that a PR is linked to an issue, labeling, checking for news entries, backporting
merged PRs to the release branches, and so on.

Yesterday I posted the announcement on the forum:
[Planned Downtime for our GitHub bots](https://discuss.python.org/t/planned-downtime-for-our-github-bots/109556). The
downtime is planned for today, Tuesday October 20, between 11 AM and 12 noon Pacific. During that hour the bots will
misbehave, or not behave at all.

#### Why now, of all weeks?

After I gave the heads-up by announcing it in the Python core devs Discord channel and on Discourse, Guido, who was
seated right next to me (I was seated in between Jacob and Guido), jokingly said something like: "On the day lots of us
are sprinting and pushing code to GitHub and making PRs, you decided to take down the infrastructure." Haha. Yeah. I
know Guido actually understands why, and he knows the value of sprinting in person. But I thought I could use my
personal blog to explain it for those who are not familiar with this type of event, and with how contributing to open
source works in general. So these are the things I considered.

Cabotage is the PSF's platform, and Jacob is the PSF's Director of Infrastructure. I have been using Cabotage for the
last year for the PyLadiesCon portal, so I am familiar with it, but I still don't feel too comfortable doing this
migration all by myself. I don't have full access rights to the various repos in the python GitHub org, and I don't have
full access rights to Cabotage either. What if some part of the migration needs higher permissions, like from an admin?
I never know until I start the process, and that is where being able to pair and sync with Jacob helps a lot. The sprint
is the one week where Jacob and I are in the same room. Throughout the day I kept asking him small questions, got
answers right away, and moved along. Asynchronously, each of those questions would have meant switching context, waiting
hours or days for a reply, then switching back. That is not optimal for either of us, and it would stretch the migration
over weeks instead of a day.

The other half of the reasoning is that the harm is bounded and fixable. The downtime won't be long. While the bots are
down, maybe a backport does not get created, or a PR does not get labelled correctly, or the news-entry check does not
run. All of that is inconvenient, and all of it can be redone once the bots are back. Nothing is lost. The one real
annoyance is that bedevere's issue-number and news checks are required on CPython PRs, so a PR pushed during that hour
will not be mergeable until bedevere is back and the check is triggered again, by redelivering the webhook or pushing
once more.

So: one hour, announced in advance, with the people who can fix things paying attention. I'll take that trade.

### Prep work before the switch

The rest of the afternoon went into getting the bot repositories ready so that the downtime hour is spent on the actual
switch, and not on discovering things that should have been done beforehand.

I'm tracking the whole migration in [Television](https://television.run/), an app I started using recently as a visual
dashboard for my coding agents (more on that below). Instead of reading through terminal output to find out what each
agent has been doing across my projects, I get a UI: one status board per project, with the open PRs, the issues, what
needs my attention, and a task list. The bot migration is the newest project on it, with a checklist grouped by bot,
then flip day, then follow-ups, 29 items in total. This is what its board looked like early in the afternoon, with
nothing ticked yet:

{{<img src="/posts/python-core-sprint-2026-day-1/images/tv/tv-migration-tracker-afternoon.png" title="CPython bots project board in Television, early afternoon: 0 tasks done, 29 open" width="640">}}

By the end of day 1, 12 of them are ticked:

- **bedevere**: rebased the Cabotage support PR ([#685](https://github.com/python/bedevere/pull/685)) onto `main`, and
  checked the environment variables in the Cabotage app, including making sure the multi-line GitHub App private key
  survived being pasted into the UI.
- **miss-islington**: fixed the lint failure and rebased [#729](https://github.com/python/miss-islington/pull/729) onto
  `main`, which had rewritten the logging setup and the worker process line underneath it. Fixed the two real blockers:
  Cabotage runs the image as the `nobody` user with no writable home, so the CPython clone and the global git config
  both failed, and the Redis connection needed to be verified against Cabotage's certificate authority instead of the
  Heroku-era "don't check the cert" override. Checked the environment variables, deployed, and let it idle. The worker
  log shows the CPython clone finishing.
- **blurb_it**: created the Cabotage application, opened the support PR (the Dockerfile needs to copy `templates/` and
  `static/` too, since the app resolves both from the working directory), set the environment variables, deployed, and
  let it idle.

{{<img src="/posts/python-core-sprint-2026-day-1/images/tv/tv-migration-tracker-night.png" title="The migration checklist in Television at the end of day 1" width="640">}}

Still open before the flip: deploying bedevere and letting it idle, replacing the Heroku section of its contributing
docs, updating the hardcoded blurb-it Heroku URL in bedevere's `news.py` (which has to ship together with the blurb_it
flip), deciding the public hostname for blurb_it, confirming the miss-islington worker pod has enough disk and memory
for a full CPython clone (cherry-picking needs history, so no shallow clone), adding a Docker build job to CI in all
three repos so a broken Dockerfile fails before deploy, and writing the runbook.

### Coming up with a plan to monitor progress

The other thing I spent time on is figuring out how we will know whether the migration is actually working, during and
after the downtime window. "The deploy succeeded" is not the same as "the bots are doing their job". Each of these bots
reacts to GitHub webhook events, so the real test is whether the right thing happens when a real event comes in.

The plan for the hour:

1. **bedevere goes first**, because it is stateless. Point the GitHub App webhook at Cabotage, watch the web log and
   Sentry, then trigger an event on a test PR and check that the label and status check show up.
2. **miss-islington second**, now that its two blockers are done. Test it with a backport label on an already-merged PR,
   and check that the backport PR appears.
3. **blurb_it last**: switch the OAuth callback URL and `APP_URL`, log in, and add a blurb to a test PR. Merge the
   bedevere URL change at the same time, so new PR comments link to the live site.
4. **Watch for a few hours**: Sentry, the process logs on Cabotage, and the GitHub App's recent deliveries page, which
   shows every webhook and whether it got a 200 back.
5. **Rollback is one line per bot**: the Cabotage URL, the Heroku URL, and where the webhook setting lives. If something
   is badly broken, flip the URL back to Heroku and we are where we started.
6. **Tell people it is done**: a comment on both PRs, a note on the Discourse thread, and a ping to the folks who have
   been reviewing and helping.

The Heroku apps stay up until a few quiet days have passed. Then they get decommissioned.

### Hallway chats

Half the value of the sprint is the conversations that happen away from the keyboard. Day 1's hallway find:
[Zellij](https://zellij.dev/), a terminal workspace and multiplexer, in the same family as tmux and screen. The pitch is
that it comes with a sensible layout, panes and tabs, and a discoverable keybinding hint bar out of the box, so you do
not have to carry around a config file you built up over a decade to make it usable.

Funny timing, because just last week at the Polyglot Unconference in Vancouver I learned about
[herdr](https://github.com/ogulcancelik/herdr), which lives in the same neighbourhood: also a terminal multiplexer, also
a single binary, but built specifically for running several AI coding agents side by side. It knows which agent is
working, which one is blocked waiting on you, and which one is done, and it keeps the sessions alive when you
disconnect. I have been using herdr for a couple of days now. It is already better than a plain terminal, and I can see
the value, but I'm not fully happy with it yet, so I'm interested in trying out Zellij. It is a general-purpose
workspace that does not know or care what is running in each pane, and I'd like to see which of the two actually sticks:
the one that is better at managing agents, or the one that is better at being a terminal.

#### A bogus Python conference

Jacob was also investigating a Python conference website that looks fake. The talk titles sound real. They sound like
talks my Python friends have given. But the speakers listed against them are people I have never heard of, and the whole
thing has that smooth, slightly-off AI-generated look. The site links to a real ticketing page where you can enter a
card number and pay money.

Not to sound arrogant, but at this point, especially for a Python conference in North America, I would recognize at
least one speaker on the schedule. I would also expect to know at least one of the organizers, through
[Conference Chats](https://www.conferencechats.org/), the community space where conference organizers hang out and
compare notes. People who know me know that I put myself out there and make the effort to engage with the wider
community through conferences, local meetups, and social media. When I look at a conference and recognize nobody, not a
speaker, not an organizer, it seems odd.

As a conference organizer, this is alarming. We already spend a lot of energy on outreach, convincing people to
register, convincing companies to sponsor. Now, on top of that, we need to prove that we are a real event and not a fake
one.

What worries me more is what this means for our community events going forward. If attendees and sponsors learn to be
suspicious of any Python conference they have not heard of, then the heuristic I used above, "do I recognize anyone
involved", becomes the bar. That bar favours events run by people who are already well connected. Does a conference now
need organizers with street credibility before anyone will trust it with their money?

I was the person on the wrong side of that bar once. When I started organizing PyCascades, my first conference, I was
not a well travelled or well known Python person. I had not spoken at many conferences. If someone had looked at our
website and thought "I don't know who this Mariatta is", we would have failed the test. We were real. We were just new.

The same bar lands on first-time speakers, and that bothers me even more. A schedule full of names nobody recognizes is
exactly what a fake conference looks like. It is also exactly what a healthy conference looks like when it is doing its
job: giving new people their first slot. Many of us gave our first talk at a regional conference, to a room of
strangers, with no footprint to speak of. If "unrecognized speaker" starts to read as "suspicious", the people who pay
for it are the ones who most need the stage, and organizers get quietly pushed toward filling their lineup with familiar
names just to look legitimate. On top of that, I know organizers are already receiving many fake, LLM-generated
proposals, which makes it harder to tell a genuine new voice from noise. Between the two, making space for new speakers
gets harder, and that undoes years of work on making conference programs more open.

I do not know how we deal with this. The fake sites will only get more convincing from here.

#### Television and telemetry

On our core dev Discord, I shared [Television](https://television.run/), the dashboard I use to keep an eye on my coding
agents' work across projects, including the bot migration. Gregory P. Smith raised a concern about data leaking to a
third-party app, and I agree with the concern. I did look into it before installing, and turned telemetry off as part of
the setup.

What I confirmed while looking:

- Television is [open source](https://github.com/telepath-computer/television), MIT licensed, so what it sends is
  readable in the source and documented in its
  [privacy notice](https://github.com/telepath-computer/television/blob/main/PRIVACY.md).
- With telemetry on, it sends anonymous usage events to PostHog in the US: server starts and upgrades, feature usage,
  coarse configuration and versions, client browser and OS family, aggregate content counts, and the name of the agent
  harness that installed it. The notice says it does not send artifact content, file paths, URLs, titles, channel names,
  names, email addresses, IP addresses or geolocation.
- With telemetry off (`tv telemetry disable`, and `tv status` confirms the opted-out state), nothing is sent.
- The server itself only listens on `127.0.0.1`, so my channels and artifacts are not reachable from outside the laptop
  unless I deliberately expose them.

So the artifacts, including the migration checklist with its environment variable names and hostnames, stay on my
machine. That was the bar I needed it to clear before using it for infrastructure work.

### Dinner

For dinner, I went with Russell Keith-Magee, Pradyun Gedam, Jacob Coffee, and Hood Chatham to a taco place around the
corner from the hotel. Counter-ordered style: you order and pay for your own food, so no bill splitting to worry about.

{{<img src="/posts/python-core-sprint-2026-day-1/images/tacos/tacodinner.jpg" title="Taco dinner" width="320">}}

---
title: "Python Core Sprint 2026: Day 3"
slug: "python-core-sprint-2026-day-3"
date: 2026-10-22T07:00:00-07:00
description:
  "Day 3 of the Python Core Sprint 2026. Closing a blurb_it pull request that would have taught contributors how to
  prompt an LLM, and writing better NEWS entry guidance in the devguide instead. A sprint leaderboard that learned to
  count more than CPython, and a session on letting triagers vote in Steering Council elections."
draft: false
menu:
  sidebar:
    name: "Python Core Sprint 2026: Day 3"
    identifier: python-core-sprint-2026-day-3
    parent: posts
images:
  - /posts/python-core-sprint-2026-day-3/python-core-sprint-2026-day-3.jpg
hero: /posts/python-core-sprint-2026-day-3/python-core-sprint-2026-day-3.jpg
tags:
  - Python
  - Open Source
  - Sprint
  - Core Dev
  - Documentation
  - Bots
  - GitHub
  - Learnings
---

Day 3 of the [Python Core Sprint](/posts/python-core-sprint-2026-day-1/), yesterday, was my last day in the room. Today
I'm traveling to Seattle for [SeaGL](https://seagl.org/), where I'm one of the keynote speakers. With the bots
[settled on Cabotage](/posts/python-core-sprint-2026-day-2/) and Heroku scaled to zero, I had the day for the smaller
things that had been waiting on the follow-up list.

### A prompt generator for NEWS entries, and why I closed it

One of the open pull requests in blurb_it was [#456](https://github.com/python/blurb_it/pull/456), from An Long (aisk),
opened back in July. It added a button to the "add blurb" page that generates a prompt. The contributor copies the
prompt into ChatGPT, Claude, Gemini, or DeepSeek, and pastes the resulting NEWS entry back into blurb_it. The prompt
includes links to the issue, the PR, the diff, and the changed files, plus the devguide's guidance on how to write a
NEWS entry.

The reasoning for the PR was that, when triaging, An noticed that many new contributors struggle to write a proper NEWS
entry, especially people who are not native English speakers or who are not used to reStructuredText. Reviewers end up
fixing the wording and the markup. And a direct LLM integration in blurb_it was correctly ruled out: we have no LLM API
credits to give away, server-side calls could be abused, and asking contributors for their own API key does not work for
most of them. Generating a prompt was the simplest thing that could possibly work.

Hugo had commented on Tuesday that he was not keen on it, expecting it would produce NEWS entries that are far too
verbose. I brought it up with the core devs in the room, and the consensus was clear: we would much rather write better
instructions for contributors, so they understand and learn how to write an effective and meaningful NEWS entry, than
write instructions on how to prompt an LLM to do it for them. The LLM-written entries we have been seeing are long. They
explain the root cause, restate the bug, and describe the tests. A good NEWS entry is one sentence.

I drafted the devguide change that night, and closed the PR with that reasoning the next morning.

### Better NEWS entry guidance in the devguide

The devguide's
[How to write a NEWS entry](https://devguide.python.org/getting-started/pull-request-lifecycle/#how-to-write-a-news-entry)
section was two short paragraphs and one example. It said to be succinct and to describe user-visible effects, and then
moved on to file format. It did not say how long an entry should be, what to leave out, or what a bad entry looks like.

[devguide #1928](https://github.com/python/devguide/pull/1928) rewrites that section:

- It explains who reads the changelog and why: people scanning it to find out whether an upgrade affects them, or to
  track down the change behind a new behavior. Most of them will not open the issue or the diff, so the entry has to
  stand alone.
- It adds a length rule. One sentence, two at most. If you need more, the change probably deserves a "What's New in
  Python" entry, where there is room to elaborate.
- It gives the shape of a good entry: start with a verb in the imperative mood that says what kind of change it is (Fix,
  Add, Remove, Deprecate), name what changed with inline markup so readers can jump to the docs, say what a user will
  notice and under which conditions, then stop.
- It lists what to leave out: implementation details and root causes, what happened before the change if the fix already
  implies it, how the problem was found, tests, benchmark figures, filler like "improves robustness", and phrases that
  refer to the PR itself.
- It replaces the old example with a real entry, followed by a longer version of the same entry, and explains why the
  longer one is worse. Nothing in the longer version is wrong. The second sentence just restates the bug that the first
  sentence already says is fixed.
- The format rules (reStructuredText, 80 columns, no leading marker) move to their own subsection.
- It adds a `news-entry-writing` anchor so that tools can link straight to the writing guidance.

{{<img src="/posts/python-core-sprint-2026-day-3/images/devguide-news-entry.png" title="The new examples section in the devguide: a preferred entry, and the same change with too much detail" width="640">}}

Stan and Carol Willing reviewed it during the day, Stan merged it in the afternoon, and it is now
[live on the devguide](https://devguide.python.org/getting-started/pull-request-lifecycle/#news-entry-writing). By the
end of the day Gregory P. Smith said on the core dev Discord that he had been telling Claude to read that PR any time he
did not like a NEWS entry, and the result was better.

Here is where I stand on all of this. I don't like writing instructions just for an LLM. As I wrote on
[claude-skills.mariatta.ca](https://claude-skills.mariatta.ca/), if I write something for an LLM, I want a human to be
able to read the same thing, understand it, and do it themselves. Writing instructions on how to prompt your LLM to
write a better NEWS entry is not what I'm after. The guidance on how to write a good NEWS entry belongs in the devguide,
where a person and an LLM can both read it.

The anchor is the piece that connects back to blurb_it. Once the devguide change merged,
[blurb_it #475](https://github.com/python/blurb_it/pull/475) added a guide above the NEWS entry field on the add blurb
form, with the short version of the same guidance: one or two sentences, start with an imperative verb, name what
changed with inline markup, say what users will notice, leave out implementation details and phrases like "this PR". It
uses the devguide's own example and links to the section for the full text. It opens for first-time visitors, and once
you collapse it, the browser remembers. The same place An's button would have gone, just pointing people at how to write
the entry instead of how to ask something else to write it. It is live on
[blurb-it.python.org](https://blurb-it.python.org/).

{{<img src="/posts/python-core-sprint-2026-day-3/images/blurb-it-news-entry-guide.gif" title="The guide on the add blurb form: open on the first visit, collapsed with a click, still collapsed after a reload, then expanded again" width="640">}}

### More blurb_it

While I was in the blurb_it templates anyway, a few more things went in:

- [#474](https://github.com/python/blurb_it/pull/474) shows the CVE field only when the Security section is selected.
  The CVE field was added on Tuesday, and the server already rejected a CVE with any other section, but the form always
  showed the field, which invited people to fill it in and then hit the error on submit.
- [#476](https://github.com/python/blurb_it/pull/476) modernizes the UI. The pages were on Bootstrap 4.1 with jQuery and
  a 2018 social buttons stylesheet. They are now on Bootstrap 5, same Pulse theme, no jQuery, with a navbar that
  collapses on small screens and a form that stacks on phones. The form's field names and values are unchanged, so the
  handler receives exactly the same data.
- [#477](https://github.com/python/blurb_it/pull/477) adds a test that the add blurb form renders. No test requested
  that page before, so a template error or a broken inline script would have passed CI. That nearly happened while
  rebasing #475: a conflict resolution truncated the CVE toggle script, and only a manual check caught it.
- I also closed [#11](https://github.com/python/blurb_it/pull/11), my own PR from December 2018, as too old and no
  longer relevant. It had been open for almost eight years.

And the last of the follow-ups from the migration landed:
[miss-islington #751](https://github.com/python/miss-islington/pull/751) removing the Heroku leftovers and moving it to
Python 3.15, and [bedevere #719](https://github.com/python/bedevere/pull/719) and
[blurb_it #472](https://github.com/python/blurb_it/pull/472) making the same move for the other two bots.

### Steering Council Q&A

In the morning there was a Q&A session with the Steering Council. I joined at the tail end of it, and overheard
mentorship and the contributing process being discussed, as well as finances and sponsorship for core Python
development. I asked for transparency in our finances. The Steering Council said the PSF keeps those records, although
they are a little behind for this year. When I looked it up after the sprint, the
[PSF public records page](https://www.python.org/psf/records/) has filings up to 2024: the 2024 annual report and the
2024 Form 990.

### Core Stars

Savannah Ostrowski built a leaderboard for the sprint: [Core Stars](https://core-stars.fastapicloud.dev/). It gives a
point for every issue or PR you close, every PR you open, and every PR you review, for the week of the sprint, and ranks
the core team and triagers. It refreshes every twenty minutes. The fine print says it is a fun sprint tally and does not
measure collaboration or the size of a contribution, which is the right disclaimer.

When it first went up, it only tracked contributions to the CPython repository. I was number 26, in the bottom three.
Then Itamar Oren suggested expanding it to the other repositories in the python GitHub organization, and Savannah did.
Now I'm number 5.

{{<img src="/posts/python-core-sprint-2026-day-3/images/core-stars.png" title="Core Stars, after it started counting every repository in the python organization" width="640">}}

Nothing about my work changed between those two numbers. What changed is what counted. Of my points this week, five came
from CPython: merging the datetime docs PR, and reviewing and merging its two backports. The rest came from blurb_it,
miss-islington, bedevere, and the devguide. The bots migration alone was more than a dozen merged pull requests across
three repositories, and the first version of the board could not see any of it.

This is something I want to ponder on. When the only thing that counts is contributions to the CPython repository,
everything else becomes invisible, and the people doing it look like they are not doing anything.

This is one thing I have been struggling with. Every now and then I too think maybe I'm not really a core dev, because
most of the work I do is not in CPython itself. I put "Python core developer" on my bio and my conference badges as a
way to reassure myself that I am one.

I find this is often the case when it comes to CPython contributions, even in the way we promote people. If a
contributor came in nowadays and contributed only to bedevere or miss-islington, they probably would not be considered
for triager or core dev, not until they actually contributed to CPython. We like to tell people that you can contribute
to Python in many ways, yet in reality, contributions to certain areas seem to matter more than others.

I appreciate that Itamar noticed and suggested that the board count more than CPython contributions. And thank you,
Savannah, for building it, and for changing it.

### Triagers on the Steering Council voter roll

At 3:30 PM I ran a discussion session on expanding the Steering Council voter roll to include triagers. In August 2024 I
had [asked on Discourse](https://discuss.python.org/t/should-we-expand-the-voter-pool-for-the-sc/62060) whether we
should expand who votes for the Steering Council, and that thread converged on one group: triagers. The session was my
attempt to turn that into a concrete proposal.

The proposal is a narrow PEP 13 amendment: active triagers get a ballot in Steering Council elections, and nothing else
changes. They would not nominate candidates, vote on PEP 13 changes, vote on new core devs, or vote on no-confidence
motions. To be on the roll, a triager would need to have been on the triage team for at least six months when the roll
is cut, affirm their intent to vote before the cut-off, the way the Packaging Council does under PEP 772, and meet the
same two-year activity standard that PEP 13 already applies to core devs. Not for the election coming up this winter,
but for the one after, in late 2027.

To me, in the age of LLM slop contributions, I find it hard to trust new contributors. I look at every new PR with
scrutiny. I think it is more important than ever that we form more trust among us, and between us and the contributors.
Unlike my initial proposal back in 2024, which also considered PSF Fellows and third-party maintainers, I feel triagers
are the natural choice. They are the people we already trust.

The room had somewhere between fifteen and twenty people, both triagers and core devs, mostly core devs. Most people
hesitated because of the existing process: they like the idea, but they want to see the criteria for who counts as an
active triager, and for who gets to become a triager, further defined and tightened first. Right now it takes a single
core dev vouching for you, and it was made that lightweight on purpose. The Python triage team was something I proposed
back in 2019. It was meant to give people a way to contribute, to recognize them, and to enable them to continue
contributing, and the lightweight process came out of
[that discussion](https://discuss.python.org/t/criteria-for-promoting-people-to-the-python-triage-team/2105/6). There
was also the concern of what happens if core devs promote their friends into triagers to get more votes. From there, the
session drifted into the requirements for becoming a triager and a core dev in general, rather than whether we can trust
triagers to vote, and then into the mentorship process. A thirty-minute session became ninety minutes. For now, the plan
coming out of the room is to tighten the triage process and raise that bar.

I need time to digest and reflect on this, and to see it apart from my personal feelings. The outcome also feels further
away from the initial wish I brought up in 2024. I think more people deserve to have their voice heard and be part of
Python without needing to be on the core team. That is the point of view I'm looking at this from. I see the core devs
looking at it from a different angle. I recognize that we are looking at this from different points of view. I will be
thinking more about this.

### Dinner and ice cream

After the sprint day I went out for dinner with Russell Keith-Magee, Kattni, Zachary Ware, and Eric Snow. Then we went
for ice cream, and took an [ice cream selfie](/posts/ice_cream_selfies/).

{{<img src="/posts/python-core-sprint-2026-day-3/images/ice-cream-selfie.jpg" title="Ice cream selfie with Russell, Kattni, Zach, and Eric" width="640">}}

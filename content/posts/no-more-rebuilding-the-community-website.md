---
title: "No More Rebuilding the Community Website"
date: 2026-08-17T09:00:00-08:00
weight: 20
draft: true
menu:
  sidebar:
    name: "No More Rebuilding the Community Website"
    identifier: no-more-rebuilding-the-community-website
    weight: 20
description:
  "I've been building a website theme for meetups and communities for the past few months. Version 0.11.0 is out today,
  and I'm ready to share it."
tags: ["Popular", "Open Source", "Hugo", "Astro", "Community", "No more spreadsheets"]
---

I've been building a website theme.

It's called Popular, it's for meetups and community groups, and
[0.11.0](https://github.com/Mariatta/hugo-theme-popular/releases) shipped yesterday. It's the release where I stopped
thinking of it as my thing and started thinking of it as something other people could pick up, so I'm finally telling
people about it properly.

## Why a theme

The short answer: there wasn't one.

When PyLadies Vancouver needed a website, I spent hours going through themes looking for something that fit a community
group. I landed on one adapted from Hinode, and I was never quite happy with it. When PyLadiesCon decided to redesign
into Astro, we spent another round of cycles building it from scratch. Then PyPodcats needed a site. Then the PyCon US
Maintainer Summit needed one. Each time I could have just reused the PyLadies Vancouver setup, and each time I didn't
want to, because I wasn't happy with it in the first place. So I went back to researching themes, adjusting, modifying,
and ending up somewhere slightly different again.

Four communities. Four rounds of the same work. None of it was the work of running a community.

This shouldn't be hard. We shouldn't be reinventing a community website every single time one is needed. Organizers
should be spending their hours writing content and engaging with their members, not rebuilding the site that announces
the thing they'd rather be doing.

And it isn't only the building. The pattern after that is always the same too. A volunteer who knows some HTML puts
something together. It works. Then the event details live in one place and the code of conduct lives in another and the
venue instructions live in a chat message from four months ago. Then that volunteer moves on, and the next organizer
opens the repo, doesn't recognize anything, and starts over.

I've been that volunteer. I've also been the next organizer.

So I set out to build the thing I kept not finding, taking from the years I've spent running and leading communities,
and putting in the parts communities actually need to be successful rather than the parts that make a nice landing page.
A theme that assumes the handoff.

Popular is the manifestation of that. And I didn't dogfood it on one community and call it proven. I put it into several
of mine, in different shapes, adjusting it and adding what was missing each time.

## What it does

Popular ships the parts a community site actually needs.

Events that split into upcoming and past on their own. Speaker profiles. Venue pages carrying the buzz code, the transit
note, the parking situation and whether the room is wheelchair accessible. A blog with multiple authors and space for
guest writers. An organizers page. A docs area for the handbook and the runbooks, with checklists that remember where
you left off. A calendar feed, so members subscribe once and every future meetup shows up in their calendar app.

Every colour and font comes from your config, so you can rebrand the whole thing without opening a CSS file. If an image
on your site is missing alt text, the build fails.

It exists twice, once for Hugo and once for Astro, released together with an identical changelog. I did that because I
didn't want to tell a community that their choice of static site generator decides whether they get a calendar feed.

It's named after the Darren Hayes song, because that's how I name things, and I'm not going to apologize for it.

## I made myself the first user

I moved my own things onto it one at a time, and let each one break it.

**[PyLadies Vancouver](https://vancouver.pyladies.com)** went first. Ten years of meetups, real speakers, real venues,
real accessibility information that people need before they can decide whether they can come. Also a rotating group of
organizers who didn't build the site and should never have to understand it. That site is where the venue and access
model got serious, and where I stopped treating the handbook as something you write later.

**[PyPodcats](https://pypodcats.live)** went next and immediately broke an assumption I didn't know I was making. A
podcast is not a meetup. An episode is not an event. A guest is not a speaker. I had named every section after the thing
I personally do, which is run meetups, and the theme quietly demanded everyone else do the same. That's why sections are
renameable now.

**[My Claude skills site](https://claude-skills.mariatta.ca)** went third, on Astro, installed as a package. Almost
entirely documentation, with no events at all, which turned out to be its own category of broken. Empty states rendered
where there was nothing to be empty about. Links pointed at the wrong place when the site lived on a subpath.

My four demo sites never found any of those bugs, because I wrote the demos, and I wrote them to fit. It's very easy to
build a tool that works perfectly on the one example you invented while building it.

## The one that convinced me it holds

The **[PyCon US Maintainer Summit](https://pycon-maintainer-summit.github.io)** site is the deepest port, and it's the
reason I'm comfortable saying the content model has settled.

The summit has eight editions going back to 2019, each with its own speakers and topics, which is nothing like a single
rolling meetup calendar. So that site replaces the theme's entire event model and all of its routes, keeps its own URLs,
and layers PyCon blue and Python yellow over the theme's components. It installs the theme from npm rather than
vendoring it, which means theme updates are a version bump instead of a git merge and an argument.

The port kept handing me bugs to fix upstream. Prose links that didn't look like links. Docs pages ordered wrong. Tag
slugs that didn't match Hugo's. Those fixes are in the theme now, which means they're in your site too, and you never
had to find them.

Then the part I didn't expect to matter so much. I upgraded that site across five releases at once, from 0.7.0 to
0.10.0. I changed the version number in `package.json` and nothing else. No config change, no component change, no
content change. I built it on both versions and diffed the output, and the HTML was identical once I normalised the
asset hashes.

That's what a stable content model looks like from the outside. Not a promise in a README. A heavily customized site
skipping five releases and not noticing.

That site is live now, in its own GitHub org, run by its own organizers. Which is the actual test: it isn't my site
anymore.

## 0.11.0, not 1.0

I want to be accurate about what this release is.

Popular is still 0.x. The number that would tell you the content model and the brand keys are frozen is 1.0, and I
haven't earned that yet. What I have is the evidence above: four of my own sites on it, one of them heavily customized
and skipping five releases without noticing. When I'm confident that holds for sites I didn't build, I'll cut 1.0, and
that's the point where breaking the content model becomes a 2.0 with a migration guide instead of a line in a changelog.

Until then, 0.x minor releases can contain breaking changes, and the changelog calls them out when they do.

What landed in 0.11.0 specifically: `npm create popular-site@latest`, which scaffolds an Astro site that _depends on_
the theme instead of containing a copy of it, so updating is `npm update` rather than diffing tags and re-copying files.
And a small thing I care about more than it sounds: a Popular site now loads nothing from a third party at all. The last
exception was one demo pulling a font from Google Fonts. It doesn't anymore. No page of the theme, its demos, or its
docs sends a visitor's IP anywhere.

## What customizing actually costs

"Override anything you like" is the kind of claim that sounds free and is not.

The summit site forks its base layout to get a richer SEO head. Which meant that when I shipped structured data in
0.6.0, that site got none of it. It couldn't. It had opted out of that file months earlier. I had to go port it in by
hand, page type by page type, and it still carries local copies of two helper files because the package doesn't export
them yet.

That's the deal with every override in every theme everywhere. The moment you fork a file, it stops receiving fixes and
becomes yours. Popular doesn't make that go away. It tries to keep the number of files you have to fork small, so the
bill stays small.

## Two that did not work

I moved four sites onto this theme. I tried to move six.

**My own site, the one you're reading, stayed where it is.** It has a talks page, a projects page, a running Ice Cream
Selfie archive and a #TypoOfTheDay archive, and every one of those is a slightly different shape I invented for myself
over years. None of them are events. None of them are blog posts, quite. Porting it wouldn't have been a port, it would
have been a rewrite, and at the end I'd have a site that fit my theme instead of a theme that fit my site. So I stopped.

**The Python Docs Editorial Board site doesn't fit either.** That one is a working group publishing documents and
decisions. No events, no speakers, no venues, no recaps. Almost everything Popular is good at is dead weight there. It
runs on PaperMod, and PaperMod is the right answer for it. I'm not moving it just to raise my own adoption count.

I'm saying this in the announcement on purpose.

Popular is for groups that have things that happen, things they write down, and people who run it. If your site is a
personal archive of a dozen bespoke collections, or a document repository with no community calendar attached, this
theme will fight you, and the fight will look like a hundred small frictions rather than one clear no. That's worse than
a clear no. So here's the clear no.

A theme that fits everything fits nothing.

## It works whether a human or an agent sets it up

It's 2026. A lot of people are going to point an AI agent at this theme and ask it to build them a site. That's just
true, and pretending otherwise would make the theme worse for them.

So both repos ship an `AGENTS.md` with a setup protocol. Point your agent at it and it will interview you
conversationally, write your answers to a file, run the same setup wizard you would run by hand, show you the diff, and
only then apply it. It doesn't hand-edit your config, because the script is the tested path and hand-edits skip the
record of what was decided.

Every site the theme builds also publishes an `/llms.txt`, so an agent reading on someone's behalf can find your next
event without guessing.

But I want to be careful here, because there's a version of this I don't want to build.

Being able to use an AI agent is a privilege. It costs money. It needs a decent machine and a decent connection. Plenty
of workplaces don't allow it, plenty of people can't afford it, and plenty of the world is not being sold it in the
first place. If setting up a community website starts to require a paid subscription to something, then I've taken a
tool any volunteer could pick up and quietly put it behind a gate.

It's also a personal choice. People have reasons for not working this way. Environmental reasons, labour reasons,
licensing reasons, or just not wanting to. Those reasons are theirs and I'm not interested in arguing anybody out of
them in a release announcement.

So: agents are supported, and agents are never required. The setup wizard is a single Python 3 script with nothing to
install, and it runs interactively for a person exactly as well as it runs from an answers file for a tool. Skip the
wizard entirely, edit the config by hand, and you get the same site. Everything the wizard writes, you can write
yourself, and the docs tell you where.

The rule I'm trying to hold to: if something works because an agent reads it, a person has to be able to read the same
thing and do it themselves. No agent-only version. No human-only version. The `AGENTS.md` turned out to be the fastest
orientation for a new human contributor too, which I didn't plan and am pleased about.

I want this theme to be available however you choose to build. Not just the way I happen to work.

## Try it

Everything is at [popular.mariatta.ca](https://popular.mariatta.ca): the docs, and four complete demo communities that
are all the same theme with different configs. An aquarium club, a foodie club, a KDrama fan club, and one very
committed superfan.

Getting to a running site takes about five minutes either way. Add the theme, copy an example, run the setup wizard or
skip it entirely.

Then tell me where you got stuck. I mean this specifically: the command that errored, the step that was out of date, the
sentence you had to read three times. Setup friction is a bug. I would much rather fix it than have you quietly work
around it and conclude you're bad at this.

I don't know how many communities will use this. That was never really the measure. I built the thing I wished existed
the first time someone handed me a community and a domain name and wished me luck.

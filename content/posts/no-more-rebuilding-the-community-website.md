---
title: "No More Rebuilding the Community Website"
subtitle: "Introducing Popular: Hugo and Astro theme for community groups and meetups"
date: 2026-08-18T09:00:00-08:00
weight: 20
draft: true
menu:
  sidebar:
    name: "No More Rebuilding the Community Website"
    identifier: no-more-rebuilding-the-community-website
    weight: 20
description:
  "I've been building a website theme for meetups and communities for the past few months. Version 0.11.0 is out now,
  and I'm ready to share it."
tags: ["Popular", "Open Source", "Hugo", "Astro", "Community", "Infrastructure"]
images:
  - /images/posts/no-more-rebuilding-community-website.png
hero: /images/posts/no-more-rebuilding-community-website.png
---

I've been building a website theme.

It's called _Popular_, after the song [Pop!ular](https://www.youtube.com/watch?v=psT28-j8atg) by Darren Hayes. A theme
whose whole job is helping small communities put on a good show deserved a name with some sparkle. It's for meetups and
community groups, and [0.11.0](https://github.com/Mariatta/hugo-theme-popular/releases) just shipped.

The official announcement, with the feature tour and the demos, is over on the theme's own site:
[Introducing Popular](https://popular.mariatta.ca/blog/introducing-popular/). This post is the other half of it. Why it
exists at all, what it cost, and who it isn't for.

I haven't said much about it until now, and not because it was secret. It's been public on GitHub the whole time. It's
because I had a fairly specific picture in my head of what this theme needed to be, and for a long stretch the thing on
disk was not that thing yet. Half of the plan was built and the other half was still a list.

A half-finished theme is not a small gift to hand somebody. It looks like help and then it isn't: an organizer gets a
site up, and three weeks later needs the venue page or the calendar feed I had been picturing all along but hadn't
written. I've been on the receiving end of that with other people's projects and I didn't want to do it to anyone.

So I kept building instead of announcing. Until 0.11.0.

This is the release where I looked at the theme and felt proud of it. Not "this is a neat thing I made on weekends"
proud, but proud enough to tell other people to use it. To recommend it to an organizer I respect, and mean it. That's a
different bar, and it's the one I was waiting for.

That confidence isn't a feeling I talked myself into. Four of my own community sites run on this thing, in front of real
members, through real events, with organizers who are not me editing the content. When something went wrong, it went
wrong on my sites first, and I fixed it in the theme rather than around it.

So I'm ready to share it now.

## Why a theme

The short answer: there wasn't one.

When PyLadies Vancouver needed a website, I spent hours going through themes looking for something that fit a community
group. I landed on one adapted from [Hinode](https://gethinode.com/), and I was never quite happy with it. When
PyLadiesCon decided to redesign into Astro, we spent another round of cycles building it from scratch. Then PyPodcats
needed a site. Then the PyCon US Maintainer Summit needed one. Each time I could have just reused the PyLadies Vancouver
setup, and each time I didn't want to, because I wasn't happy with it in the first place. So I went back to researching
themes, adjusting, modifying, and ending up somewhere slightly different again.

Four communities. Four rounds of the same work, none of it the work of running a community. This shouldn't be hard.
Organizers should be spending their hours writing content and engaging with their members, not rebuilding the site that
announces the thing they'd rather be doing.

Some communities have a web designer, somebody who volunteers their craft and works out a look with the organizers.
That's a real resource and it shows. I don't have that, and most of the volunteer-run open source communities I've been
part of don't either. Local Python meetups. PyLadies chapters. The small user groups that put on an evening with two
talks and some pizza. Most of the ones I know are struggling to find volunteers at all, and the organizers I know are
tired, a lot of them burned out, holding a group together on evenings and weekends after a full day of paid work.

I once told a community that it was time they had a website. The first thing raised back at me was not "who will build
it." It was: "but then we have to maintain it."

That's the real objection, and it's a fair one. Maintaining a website is a genuinely fun hobby for some people. For
plenty of others it's a chore that arrives every month forever, one more thing to feel behind on. Me too, honestly: I
want to focus on the content, not the tooling or the CI or the workflow. So the bar I set was not "can somebody build a
site with this." It was: can somebody keep it going on the worst week of their year, and hand it to the next person
without a handover meeting.

Then there's money. The same communities that need a website, and have no one to maintain it, also run on zero dollars.
Not a small budget. Zero. What a community in that position can do is put a static site on GitHub Pages, which costs
nothing and stays up, and that means the answer had to be a static site generator rather than a platform with a monthly
plan and a login. The two I keep seeing, and the two I use myself, are Hugo and Astro. Which is why the missing piece
was a theme. Not a product, not a service, not a thing I host for you.

There's one more thing a theme has to survive: what happens to a site after it's built. A volunteer who knows some HTML
puts something together. It works. Then the event details live in one place, the code of conduct in another, and the
venue instructions in a chat message from four months ago. Then that volunteer moves on, and the next organizer opens
the repo, doesn't recognize anything, and starts over.

I've been that volunteer. I've also been the next organizer. So I set out to build the thing I kept not finding, taking
from the years I've spent running and leading communities: a theme that assumes the handoff. _Popular_ is the
manifestation of that.

## What it does

_Popular_ ships the parts a community site actually needs. These aren't page templates you have to wire up. They're a
[content model](https://popular.mariatta.ca/docs/content-model/) built into the theme: you fill in the fields, and the
pages, the links between them and the listings build themselves.

- **[Events](https://popular.mariatta.ca/docs/content-model/#events)** each carry a date, and the theme sorts them into
  upcoming and past from that, automatically. Nobody has to remember to move anything to an archive, and your site never
  sits there advertising a meetup that happened last week.
- **[Speakers](https://popular.mariatta.ca/docs/content-model/#speakers)** are their own records. A person's bio and
  photo are written once and appear on every event they're part of.
- **[Venues](https://popular.mariatta.ca/docs/content-model/#venues)** have fields for the buzz code, the transit note,
  the parking situation and whether the room is wheelchair accessible. An event links to its venue instead of repeating
  half of it and getting it wrong.
- **[Blog posts](https://popular.mariatta.ca/docs/content-model/#authors)** support multiple authors, with room for
  one-off guest writers.
- **[Organizers](https://popular.mariatta.ca/docs/content-model/#organizers)** get a page, so members know who is
  actually running this, and who to talk to when they need help, want to give a talk, or want to sponsor.
- **[Docs pages](https://popular.mariatta.ca/docs/content-model/#docs-pages-handbook--runbooks)** hold the handbook and
  the runbooks, with
  [checklists that remember where you left off](https://popular.mariatta.ca/docs/components/#checklist-persistent).
- **[A calendar feed](https://popular.mariatta.ca/docs/configuration/#calendar-feed-ical)** comes out of your events, so
  members subscribe once and every future meetup shows up in their calendar app.

Every colour and font comes from [your configuration](https://popular.mariatta.ca/docs/theming/), so you can rebrand the
whole thing without opening a CSS file. If an image on your site is
[missing alt text](https://popular.mariatta.ca/docs/migrating-images/#alt-text-is-required), the build fails.

"Re-brand it from the configuration" is easy to say and hard to believe, so the theme ships with four demo sites to show
it: complete, fictional communities running identical theme code with different configurations. An aquarium club, a
foodie club, a KDrama fan club, and one very committed superfan. They don't look like the same website wearing four
hats, and they're there to copy from rather than starting at a blank directory.

And a small thing I care about more than it sounds: a _Popular_ site loads nothing from a third party at all. No fonts
from a font host, no scripts from a CDN, nothing that quietly tells someone else that a member of your community visited
your page. No page of the theme, its demos, or its docs sends a visitor's IP anywhere.

_Popular_ is available for both Hugo and Astro static sites, released together with an identical changelog. I like both
frameworks, I keep seeing people in my communities using both, and I'd rather ship the theme twice than tell somebody
their choice of framework decides whether they get a calendar feed. A
[parity contract](https://github.com/Mariatta/hugo-theme-popular/blob/main/PARITY.md) holds the two together: change
something in one and the other gets it in the same release, not eventually. It's a discipline I hold myself to, because
the alternative is a second-class version, and whoever ends up on it didn't choose to be there.

## I made myself the first user

One at a time, I ported the websites I own and manage over to the theme, adapting each one until it fit, and letting
each one break the theme on the way.

These weren't test cases I picked for being convenient. They're every community and project I'm involved in that has, or
needs, a static website. Six of them, all real, all with members and readers who would notice if I got it wrong. If the
theme was going to fall apart somewhere, I wanted it to fall apart in front of me first.

**[PyLadies Vancouver](https://vancouver.pyladies.com)** went first, in
[July](https://github.com/pyladies-vancouver/pyladies-vancouver.github.io/pull/13). Ten years of meetups, real speakers,
real venues, real accessibility information that people need before they can decide whether they can come. Also a
rotating group of organizers who didn't build the site and should never have to understand it. That site is where the
venue and access model got serious, and where I stopped treating the handbook as something you write later.

**[PyPodcats](https://pypodcats.live)** went next, [later that month](https://github.com/psf/the-invisibles/pull/88),
and immediately broke an assumption I didn't know I was making. A podcast is not a meetup. An episode is not an event. A
guest is not a speaker. I had named every section after the thing I personally do, which is run meetups, and the theme
quietly demanded everyone else do the same. That's why sections are renameable now.

**[My Claude skills site](https://claude-skills.mariatta.ca)** went third,
[in August](https://github.com/Mariatta/claude-skills/pull/2), on Astro, installed as a package. This one wasn't a
community site at all: almost entirely documentation, no events, no speakers, no venues. I did it to push the theme to
its limit and see how far it would go before it stopped making sense. It went further than I expected, and the result is
a real docs site I actually use. It also found its own category of bugs: empty states rendered where there was nothing
to be empty about, and links pointed at the wrong place when the site lived on a subpath.

The demo sites never found any of those bugs, because I wrote the demos, and I wrote them to fit. It's very easy to
build a tool that works perfectly on the one example you invented while building it.

## The one that convinced me it holds

The **[PyCon US Maintainer Summit](https://pycon-maintainer-summit.github.io)** site is the deepest port, landing
[two days before this release](https://github.com/pycon-maintainer-summit/pycon-maintainer-summit.github.io/pull/3), and
it's the reason I'm comfortable saying the content model has settled.

A summit is not a meetup. A meetup repeats: same group, same rhythm, one rolling list of who organizes and who speaks.
The summit happens once a year and reinvents itself each time. The format changes between editions. There's a call for
proposals per summit rather than one standing invitation. The speakers and organizers belong to the year they showed up
for, and they should be credited there, not folded into a permanent roster.

My theme had an opinion about every one of those things, absorbed from running monthly meetups without noticing I'd made
them. Each place the summit didn't fit was a place the theme was narrower than it needed to be, so I fixed those
upstream rather than patching around them. The theme bends now where it used to be rigid, and your site gets that
without ever having to find out why.

It's also why I trust the content model. That site has since skipped five releases in a single upgrade and needed no
changes of its own to keep working. Not a promise in a README. A heavily customized site skipping five releases and not
noticing.

It's live now, in its [own GitHub org](https://github.com/pycon-maintainer-summit), where the organizing team maintains
it together.

## 0.11.0, not 1.0

I know a 0.x version number gives people pause. It reads as "not finished," and nobody wants to build their community's
website on something that might move under them.

So let me say what the number actually means here. _Popular_ is still 0.x because I'm hoping for feedback, and because I
don't think a version number should be declared stable on the strength of one person's opinion. My own evidence is real,
but it isn't the same as knowing it holds for a site I didn't build, for a community I'm not part of, with needs I
didn't think of.

The 0.x is not me keeping a door open so I can walk away from responsibility later. It's the opposite. It's the window
where your feedback can still change the shape of this thing, before the content model is frozen and changing it costs
everyone a migration. Tell me what's missing and it can still get in. That's how this becomes something built for the
community, rather than a thing I made and handed down.

When I'm confident it holds for people who aren't me, I'll cut 1.0. Until then, every change goes in the
[changelog](https://popular.mariatta.ca/changelog/), in plain language, so you can always see what moved before you
update.

And if it turns out that no community other than my own ever finds this useful, then so be it. My own communities have a
theme they no longer have to rebuild, which was the point I started from.

## Not for everything, on purpose

Four sites ended up on this theme. I actually tried to move six. The other two just didn't work out, so I abandoned that
effort.

**My own site, the one you're reading, stayed where it is.** It has a talks page, a projects page, a running Ice Cream
Selfie archive and a #TypoOfTheDay archive, and every one of those is a slightly different shape I invented for myself
over years. None of them are events. None of them are blog posts, quite. Porting it wouldn't have been a port, it would
have been a rewrite, and at the end I'd have a site that fit my theme instead of a theme that fit my site. So I stopped.

**The [Python Docs Editorial Board](https://python.github.io/editorial-board/) site doesn't fit either.** That one is a
working group publishing documents and decisions. No events, no speakers, no venues, no recaps. Almost everything
_Popular_ is good at is dead weight there. It runs on [PaperMod](https://github.com/adityatelange/hugo-PaperMod), and
PaperMod is the right answer for it. I'm not moving it just to raise my own adoption count.

I'm saying this in the announcement on purpose.

_Popular_ is built for one kind of thing, and it's the kind I know: meetups and community groups. A user group that
gathers every month. A local chapter. A club. A fan community. An annual gathering that comes back every year. If your
group meets, invites people to come, has speakers or hosts or organizers, and wants members to find out where and when
without asking in chat, that's the shape the whole theme is cut to.

If your site is a personal archive of a dozen bespoke collections, or a document repository with no community calendar
attached, this theme will fight you, and the fight will look like a hundred small frictions rather than one clear no.
That's worse than a clear no. So here's the clear no.

A theme that fits everything fits nothing.

## It works whether a human or an agent sets it up

It's 2026. A lot of people are going to point an AI agent at this theme and ask it to build them a site. That's just
true, and pretending otherwise would make the theme worse for them.

So both repos ship an `AGENTS.md` with a setup protocol. Point your agent at it and it will interview you
conversationally, write your answers to a file, run the same setup wizard you would run by hand, show you the diff, and
only then apply it. Every site the theme builds also publishes an `/llms.txt`, so an agent reading on someone's behalf
can find your next event without guessing.

But there's a version of this I don't want to build. Being able to use an AI agent is a privilege. It costs money, it
needs a decent machine and a decent connection, plenty of workplaces don't allow it, and plenty of people can't afford
it. It's also a personal choice, and people have reasons for not working this way: environmental, labour, licensing, or
just not wanting to. If setting up a community website starts to require a paid subscription to something, then I've
taken a tool any volunteer could pick up and quietly put it behind a gate.

So: agents are supported, and agents are never required. The setup wizard is a single Python 3 script with nothing to
install, and it runs interactively for a person exactly as well as it runs from an answers file for a tool. Skip it
entirely, edit the configuration by hand, and you get the same site.

The rule I'm trying to hold to: if something works because an agent reads it, a person has to be able to read the same
thing and do it themselves. No agent-only version, no human-only version. I want this theme to be available however you
choose to build, not just the way I happen to work.

## Try it

**If you're running a community and you've been meaning to refresh the website**, the one nobody has touched since the
volunteer who made it moved on, go have a look. Bring your events, your speakers, your venues, your handbook. That is
the shape this thing was built around.

**If you're starting a community and you don't know where to begin**, start here. You do not need to make the same
research detour I made four times. Pick a demo that looks closest to what you're doing, change the name and the colours,
and you have a site.

**And if you know a community that doesn't have a website, or has one that's quietly falling apart, send them this
post.** Most of the organizers I'm trying to reach are not reading theme release notes. They're running the thing. They
find out about tools because somebody in their group says "hey, this might help."

Everything is at [popular.mariatta.ca](https://popular.mariatta.ca): the docs, and the four demo communities, live and
clickable.

Getting to a running site takes about five minutes, and the [quick start](https://popular.mariatta.ca/docs/quick-start/)
walks the whole thing. On Astro, `npm create popular-site@latest` scaffolds a project that _depends on_ the theme
instead of containing a copy of it, so updating later is `npm update` rather than diffing tags and re-copying files by
hand. On Hugo, add the theme as a module and copy one of the example sites. Either way, run the setup wizard for your
name, colours and links, or skip it and edit the configuration yourself.

Then tell me where you got stuck. I mean this specifically: the command that errored, the step that was out of date, the
sentence you had to read three times. Setup friction is a bug. I would much rather fix it than have you quietly work
around it and conclude you're bad at this.

I don't know how many communities will use this. That was never really the measure. I built the thing I wished existed
the first time someone handed me a community and a domain name and wished me luck.

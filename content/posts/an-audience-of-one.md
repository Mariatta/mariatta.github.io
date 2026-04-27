---
title: "An Audience of One"
date: 2026-04-27T08:00:23-07:00
weight: 20
draft: false
menu:
  sidebar:
    name: An Audience of One
    identifier: an-audience-of-one
    parent: posts
tags: ["Conference", "PyCon", "PyladiesCon", "No more spreadsheets", "Infrastructure", "Public Speaking"]
images:
- /images/posts/audience-of-one.png
hero: /images/posts/audience-of-one.png
---


# An Audience of One

I gave a talk at a regional conference this past weekend. I prepared for it the same way I prepare for
any other talk or keynote: rehearsed it multiple times, reviewed the material, made adjustments so it would
be relatable for this audience instead of giving the same speech everywhere.
I looked up [ice cream selfie](/posts/ice_cream_selfies) locations near the in the area.

Whether there would be anyone in the room to hear it was a different question.

One person showed up at the start. Another wandered in ten minutes before the end, surprised to find anyone in
the room at all.

This is the story of how that happened. The irony: the talk I gave in that room, *No More Spreadsheets*,
is about solving exactly this kind of problem, and why we're building **real** conference infrastructure for PyLadiesCon.

---

Less than 24 hours before the conference starts, one of the organizers reached out: would I be okay moving my talk to
an earlier time slot and a different room, in a different building? I said yes immediately.

I've organized nine conferences. I know what that message costs to send. Organizers do not enjoy changing schedules at
the last minute. If they're asking, it's because they've already tried everything else and run out of options.
You don't reach out to a speaker the day before and ask them to move for no good reason.

So I said yes. I checked the conference website and saw the update reflected there. The morning of my talk, 
I came in early, checked in at the speaker desk. They looked at the printed out speaker scheduling spreadsheet. It
has the new room and the new time slot. Everything is confirmed. Everything agreed. I'll be speaking in the new room
at the new time.

I went to the room 15 minutes early, as requested in the speaker information email. When I got to that room to
set up my laptop, I looked at the printed sign on the door. The talk before mine was on it. The talk after mine was on
it. My talk, in the slot between them, was not.

It wasn't that the sign was wildly out of date. It was that my slot, specifically, was a hole. To anyone walking past,
the room had a session, then nothing, then another session. A blank space where I was supposed to be.

The host came in, ready to help set up the next session. Mine, in their understanding. They knew. I knew.
The website knew. The speaker desk knew. The piece of paper taped to the wall did not know, and the attendees who
walked past that piece of paper had no reason to doubt the paper.

One person came on time. Another came ten minutes before I finished, because they thought the room was empty. They didn't
see the schedule on the paper, and thought perhaps it's just a break between sessions. Perhaps it was just someone
doing a talk rehearsal. Perhaps the session was canceled. To them, the paper outside the room is the truth.

Nobody did anything wrong. The signs were printed at some point, with the right information available at that time.
The reschedule was updated at the source: at the website and conference scheduling app. The conference website
was the source of truth. Not the paper printout. But if an attendee doesn't know it, when there's a confident printed
schedule right in front of them, then the source of truth might as well not exist.

The irony is not lost on me.

This year I've been giving a talk called *No More Spreadsheets* at conferences around the Python community. You
can still catch it at [PyCon US in May](https://us.pycon.org/2026/schedule/presentation/80/). It's about why conference
organizers and the volunteers who hold these events together deserve better tools than the patchwork of docs, sheets,
manually copy-pasted messages, all scattered across all the tools we currently rely on. It's a big part of why we built the
[PyLadiesCon](https://conference.pyladies.com/) web portal: a single source of truth for the organizers, sponsors,
speakers, and our volunteers. To keep information in sync and updates automatically, because keeping them in sync by
hand is a job that scales badly and breaks invisibly.

The room I was supposed to be in was fine. The room I was actually in was fine. Both rooms were "right" depending
on which artifact you consulted, and the gap between those artifacts is where my audience went missing.

This is what I mean when I say conferences need something better than spreadsheets. The failure mode isn't dramatic.
It's not a server going down or a registration system melting. It's a printed page that was true on Tuesday and
stopped being true on Friday, and there was no good way for the paper to know.

To the one person who came on time: thank you. You got the same talk I would have given a full room. To the person who
poked their head in at the end: thank you too. Don't worry, it was recorded.

Speaking to empty chairs takes a different kind of mental strength. I gave the talk like the room was full. I reminded
myself: it's okay. The point is to get this recorded and uploaded on YouTube later on. People watching on YouTube
couldn't tell the difference if there was real live audiences or not.

If anything, this experience left me with more empathy for volunteer conference organizers. I've helped
organize enough events to know how this goes. Speakers no-show. Speakers cancel the night before. Schedules shuffle at
the last minute because somebody's flight got delayed or the room AV doesn't work or two talks ended up in the wrong
slots.

A few times at PyLadiesCon, we've had to remove a speaker from the schedule about an hour before their live talk.
(It's part of why we moved to requiring pre-recorded talks in our second year, after a fully-live first year.)
At PyCascades one year, a speaker scheduled to present online was unreachable in the hours before their slot. Organizers
asked me to stand by as a backup speaker in case they didn't show. They did show, just a few minutes before
their scheduled talk. But I'd already watched the organizers scramble, stressed out for the whole day, for this one talk.
Worried about disappointing their audiences.

It happens at every conference, everywhere, every year. None of it is anyone's fault. It's just what running an event
in the real world looks like.

The deeper irony: my talk made the argument that conference organizing isn't *just* non-technical work. There's logic in
it. There's tech in it. There are rules and triggers and state changes hiding underneath what looks like soft,
people-shaped work.

*If* the schedule changes, *then* reprint the room signs. *If* a talk moves rooms, *then* notify everyone who marked
it in their personal schedule. *If* a speaker cancels, *then* update the website, the app, the door, the host's notes,
and the volunteer at the info desk. All of it, in one motion, without anyone having to remember which artifacts exist
or where they live.

That's not magic. That's an `if` statement. That's code. That's logic. That's a pipeline. That's the thing
programmers do every day for problems much less important than getting an audience to the right room.

To every conference organizer who has ever printed a schedule, taped it to a wall, and then watched something shift
two days later. I see you. This is hard work, often unpaid, often invisible until it breaks. You are not the problem.
The problem is that we keep asking volunteers to do this work with tools that were never designed for it, while
pretending the work itself isn't technical enough to deserve better.

Conferences need infrastructure, not improvisation.

PyLadiesCon is building ours. Learn about it at my upcoming talk
at [PyCon US](https://us.pycon.org/2026/schedule/presentation/80/).

No more spreadsheets.

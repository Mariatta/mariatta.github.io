---
title: "No More Scheduling Polls"
date: 2026-04-23T10:00:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "No More Scheduling Polls"
    identifier: no-more-scheduling-polls
    weight: 20
tags: ["Secret Codes", "MCP", "Django", "No more spreadsheets", "No more meetings"]
images:
- /images/posts/no-more-scheduling-polls.png
hero: /images/posts/no-more-scheduling-polls.png
---

As a community leader, 9x serial conference organizer, public speaker, and open source
maintainer, I often get asked by community members for a time to meet. Here's the thing:
asking me for a time to meet is, itself, a waste of time. My calendar shifts constantly: 
work meetings, family activities, conference travel, PRs to review, all of the above.
The back-and-forth to schedule a 30-minute call often takes longer than the meeting itself. By
the time you've asked and I've replied and we've gone back and forth, the slot we landed
on is already gone.

I've been annoyed about this for years. But No More.

## No More

No more up-up-down-down-left-right-left-right on my calendar trying to find a time to meet with you.

You can now see my availability for the next 14 days on my Secret Codes web app at
[secretcodes.dev/availability](https://secretcodes.dev/availability).

No login. No account. No "let me know which of these works best." Just open slots.

{{<img src="/images/secretcodes-availability.png">}}


## I'll Have Your Agent Talk to My Agent

Secret Codes also has an MCP server. If you're running an AI agent, or if you're also into workflow automation,
you can hit the MCP server instead. Point your agent at my agent and let
them figure out when we should meet. Check the docs at
[secretcodes.dev/agents](https://secretcodes.dev/agents).

### The JSON endpoint

```aiignore
POST https://secretcodes.dev/mcp/
Content-Type: application/json
```

### Using Claude Code

```
claude mcp add mariatta-availability https://secretcodes.dev/mcp/
```

### With Curl

Ask whether a specific time is free:

```
curl -sX POST https://secretcodes.dev/mcp/ \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"check_availability","arguments":{"datetime":"2026-04-25T17:00:00+00:00","duration_minutes":60}}}'
```


## Stop Asking Me for a Time to Meet

Stop asking me for a time to meet. Stop sending me scheduling polls. Stop asking me to
"pick three times that work for you next week."

If you want to meet with me, check my [availability](https://secretcodes.dev/availability) page, pick a time that works.

You can't book directly yet, but I'm working on it. But, if you already know the "real" secret code (meaning if you
already know me well enough to know my email address) then nothing stops you from sending me a calendar invite.

For others without my secret code, please: No reply-all email thread. No four-way calendar Tetris. No week-long poll
that collects responses from seven people and still lands on the one slot that doesn't work for me.

## My Other No's

{{<mastodon user="mariatta" server="fosstodon.org" id="114633155998437321">}}

I've been working towards some "nos". The one that I've been most loud about is the **no spreadsheet**, which
is already in motion. You can hear more about that in my upcoming talks at
[PyCascades](https://2026.pycascades.com/program/talks/no-more-spreadsheets-building-pyladiescon-infrastructure-with-python-and-django/),
[LinuxFest Northwest](https://lfnw.org), and [PyCon US](https://us.pycon.org/2026/schedule/presentation/80/).

You can also learn more about how I do travel planning and travel budgeting without docs and spreadsheets (fulfilling
both **no doc** and **no spreadsheet** at once), by reading my blog posts about [Travel Budgeting without Spreadsheet]({{< ref "posts/travel-budgeting-without-spreadsheet" >}})
and [Travel Planning with AI]({{< ref "posts/travel-planning-with-ai" >}}).

I didn't think I'd get to the **no when-is-a-good-time-to-meet** this soon. But now because of technology, we can
have our own personal agents. So I built it.

The reason I'm building my own, is part of another overarching goal: being in control, owning myself, my data, my code,
instead of relying on third party services. I'm choosing which ones I still rely on, and which ones I can build myself.

Some tools we keep using out of habit. Sometimes we just need to stop, and ask, is this still the right way to do things?
Time changes. We change. Our mindset changes. Our tools should change and adapt too.

The trick is pausing long enough to ask instead of just going through the motions.

If your agent wants to talk to mine, you know where to find us.
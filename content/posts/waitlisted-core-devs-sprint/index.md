---
title: "Waitlisted for the Core Devs Sprint: When the Bad News was Also the Good News"
draft: false
date: 2026-06-16T09:00:00-07:00
tags: [python, conferences, travel, budgeting, "No more spreadsheets"]
hero: /posts/waitlisted-core-devs-sprint/waitlist-hero.png
images:
  - /posts/waitlisted-core-devs-sprint/waitlist-hero.png
---

Last week, I learned that I was one of 17 people
[waitlisted for the Python Core Devs Sprint at OpenAI](https://discuss.python.org/t/2026-python-core-dev-sprint-at-openai/106928)
this year.

A waitlist that long realistically means I probably won't get in. I was sad, of course. The sprint alternates between
Europe and the US. Traveling to Europe is ... hard and complicated. I couldn't go to last year's in Europe, because of
the location and work conflict. I was really hoping to go to this year's US sprint. Next year it will be back in Europe,
out of reach again. That's potentially not sprinting for three years in a row.

(There was a consolation prize, kind of: instead of the sprint invitation email, I got 6 months of Codex Pro from OpenAI
for free. I'll take it.)

So, I decided not to hold my breath about getting added to the sprint. I know I can contribute to the Python community
in other ways.

With the Core Devs Sprint off my calendar, it actually opened up my availability for other conferences happening that
same week. Two had been on my radar:

- **[SeaGL](https://seagl.org/)** (the Seattle GNU/Linux Conference): practically in my backyard
- **[PyBeach](https://2026.pybeach.org/)**: one of only two (still active) North American Python conferences I haven't
  spoken at yet ([PyLatam](https://www.pylatam.org/) is the other).

Both were tempting.

## How I decide whether to go to a conference

Whether I go to a conference usually comes down to three things:

1. **Timing**: does it conflict with work or family events?
2. **Speaking**: do I get to give a talk? That's usually my reason to go, though pitching in another way (staffing a
   booth, joining a sprint) counts too. And a talk means a new
   [ice cream selfie](https://mariatta.ca/posts/ice_cream_selfies/) 🍦
3. **Affordability**: can I actually afford to go?

The first two aren't really things I control. The **CFP decision isn't up to me**. I submit and I hope. And **timing**
isn't fully mine to control either. But in this case, the very thing that disappointed me also cleared my calendar: with
the sprint off the table, that week opened right up.

The budget, that's a decision that's actually mine to make. And that's the interesting part.

And it's exactly the situation I built my [travel planning app](https://travel.mariatta.ca) for. Because I'd already set
up my travel site months ago, and used it for real trips, pivoting my plan was easy: the moment the sprint fell through,
I could swap in a completely different plan and see the numbers **within minutes**, instead of building a budgeting
spreadsheet and writing formulas to calculate costs and expenses.

The disappointment didn't last long. Now I get to find a different way to show up for the community.

## Letting the travel planning app do the math

Before I even submitted the talks, I spun up the trip in my planner.
[See it here](https://travel.mariatta.ca/seagl-pybeach-2026/).

I invoked a Claude slash command, a personal command I've created for myself, saying in natural language:
`/new-trip SeaGL and PyBeach in October, arriving in Seattle Thursday then fly to LA Friday evening.`. That is all. The
app understood what I meant. It was purpose-built for it. It scaffolded the whole thing as one back-to-back weekend. It
looked up the conference dates, figured out my conference tradition of incorporating ice cream selfies, then calculated
the trip budget. Two cities, three flights, two hotels, all in one itinerary.

Interestingly, this is exactly what I built the app for: multi-city travel rolled into a single budget for a single
event. (It started as a planner for my trip to Portugal,
[which you can read about here](https://mariatta.ca/posts/travel-planning-with-ai/).)

I'd been to LA twice this year alone. In March, I went there to see Darren Hayes. And I just got back from PyCon US. By
now, I'm kinda familiar with the place, I already know where I'd stay and where to eat.

Seattle, I've been to plenty of times. I was in the area for the
[2024 Python core dev sprint at Meta](https://mariatta.ca/posts/python-core-sprint-2024-day-1/).

So the usual parts of travel planning like "what can I do?" and "where should I eat or stay?" became less interesting or
useful.

But the budget, that was the part I needed, and I'm kinda proud of myself for having built that in from the get go.

And here's what it came up with for the whole trip:

| Category                            | Estimate (CAD) |
| ----------------------------------- | -------------: |
| Flights (3 legs)                    |           ~775 |
| Hotels (3 nights)                   |           ~985 |
| Food                                |           ~315 |
| Local transport & airport transfers |           ~260 |
| Misc + buffer                       |           ~210 |
| Conference tickets                  |           ~145 |
| Activities (yes, ice cream)         |            ~70 |
| eSIM                                |            ~20 |
| **Total**                           |     **~2,780** |

**$2,800 CAD.** (**2000 USD**).

With this, now the question is no longer a vague _"Can I afford it?"_, but a concrete _"Can I afford to spend 2800 for
just one weekend?"_.

Now, you might say, _"Mariatta, that number is made up and hallucinated by AI. Why would you trust it?"_

Here's the thing: **because it isn't pure hallucination anymore.** I've been logging my _real_ conference travel
expenses in the app: for LinuxFest Northwest and PyCon US. So instead of guessing, it now has actual numbers to work
from. After those trips, I exported what I'd logged and had it compare my real spending against what I'd originally
budgeted. Two patterns fell out: my **flights almost always cost more than I plan for** (so the estimates now pad them),
and **conference food depends entirely on whether the event feeds you**. For example, PyCon US served lunch, so my food
spend was low; SeaGL and PyBeach don't, so the app keeps food at the full self-paid rate instead of quietly
under-budgeting it.

**It's grounded in what I actually spent, not invented.**

The number still isn't _exact_, and it doesn't need to be. It just needs to be good enough to make a decision with, and
now it is.

But that's exactly why having it in front of me helped. I don't submit a talk unless I already know I could follow
through. I'm a conference organizer myself, so I know speaker cancellations are one of the things that stress organizers
out. Saying yes and then backing out later isn't fair to them.

The number informs my decision. It tells me how much it would cost to go to both conferences. It also gives me a sense
of the what-ifs:

- **If only SeaGL accepts**: just Seattle, a short hop from home. Then I'd be spending less than the estimated budget:
  the most affordable option.
- **If only PyBeach accepts**: just Los Angeles. This would cost more than going to SeaGL alone, but still well under
  the full 2000 bucks.
- **If both accept**: the whole two-city weekend, and the financial worst case at around $2,800.

There are two ways to see the same thing: Both talks accepted is the financial worst case, and the speaker's dream at
the same time.

Two thousand US dollars is a lot of money to be spent just for one weekend. It's basically a whole year of a Claude Max
subscription. In Canadian dollars, that's about
[two months of groceries for a family of four](https://www.dal.ca/sites/agri-food/research/canada-s-food-price-report-2025.html),
or more than a full
[month's mortgage payment](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/mortgage-and-debt/average-scheduled-monthly-payments-new-mortgage-loans)
for a typical household. I don't take it lightly, and I don't take it for granted: being able to look at a number like
that and still say yes, is a privilege, and I'm aware of that.

So the budget gave me pause, sure. But once I saw that even the worst case was a number I could live with, the decision
itself came quickly. About thirty minutes after the plan was set up, I'd submitted both CFPs.

When I learned about the waitlist, PyBeach's CFP was already down to its final day, so I scrambled to get my proposal in
just in time. It's since closed. SeaGL, on the other hand,
[extended its CFP through the end of June](https://seagl.org/news/2026/06/01/date-change-cfp-extension).

> If you'd like, you too can [submit a talk to SeaGL](https://pretalx.seagl.org/2026/cfp)!

## Moral of the Story

Bad news can be good news, depends on how you look at it. Not getting in to the exclusive Core Devs Sprint? Yeah that
sucks. But it opened up my availability for two other conferences which have always been on my radar.

Possibility of spending two grand for just one weekend, urgh... But, the most expensive version of the trip is also the
best one as a conference speaker.

The disappointment and the win were the same news. Two ways to react to the same thing. I chose to see the positive
side.

I'm personally proud that **the app I built for myself actually worked**. I get to do all this without opening up any
spreadsheets, and no formulas. Just the getting the budget I needed when I needed it.

When I first built it, it was just a planner for one trip. I had no idea where it would go, whether it would become
anything, or just be a thing I made once and forgot. But here it is, being useful: scaffolding new trips in minutes and
remembering my quirks. It saved me time _and_ helped me turn a disappointment into two conferences I'm excited about.
That feels good.

It's paying off. Every trip I record now makes the next budget a little more accurate. A travel planning and budgeting
that is highly personalized and tailored just for me.

The app is open source, and there's a [Claude skill](https://github.com/mariatta/claude-skills) if you'd like to build
your own, no budgeting spreadsheet required. (
[I wrote about travel budgeting without spreadsheet](https://mariatta.ca/posts/travel-budgeting-without-spreadsheet/).)

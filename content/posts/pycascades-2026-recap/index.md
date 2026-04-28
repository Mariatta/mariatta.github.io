---
title: "PyCascades 2026 Recap"
date: 2026-04-28T09:36:42-07:00
draft: false
menu:
  sidebar:
    name: PyCascades 2026 Recap
    identifier: pycascades-2026-recap
    parent: posts
hero: /posts/pycascades-2026-recap/pycascades2026-recap.png
tags:
  - pycascades
  - conference
  - python
  - community
  - no more spreadsheets
---

# PyCascades 2026 Recap

PyCascades 2026 took place in Vancouver this year. I only get to attend on the first day, because I had a 5 a.m. flight
to Washington DC the morning after.

Still, the first day's talks were all very insightful and interesting. I'm waiting for all the talks to be published so
that I could catch up on the ones I missed.

Here are notes on the talks I got to see.

## [Permacomputing and Python](https://2026.pycascades.com/program/talks/permacomputing-and-python/) by Łukasz Langa

Łukasz introduced the idea of _permacomputing_, borrowing from permaculture, as a way of thinking about sustainable,
dependable computing. The core idea: your devices and your software shouldn't become e-waste the moment a vendor decides
to shut something down or push you to upgrade.

He talked about the very real problem of digital assets being locked behind 2FA, subscriptions, and proprietary
services. What happens to your photos and memories when you pass on? What happens when a service is shut down for
"business reasons"? What if there's a war? What if ... ?

He recommended Michał Zalewski's book _Practical Doomsday: A User's Guide to the End of the World_.

Why is Python a good fit for permacomputing? Because Python is elegant, debuggable (`breakpoint()` is your friend), and
has a great standard library: XML, HTML, CSV, asyncio, all built in. The tradeoffs (interpreted, pointer chasing,
everything by reference) are worth it, and the language has a real commitment to backward compatibility. PEP 387 is
being extended to a 5-year backward compatibility window. Python is a public good, and that matters.

Łukasz's practical suggestions:

**As a consumer:**

- Keep backups for real
- Own your hardware, software, and data
- Question the upgrade culture
- Choose repairable products
- Cull software subscriptions
- Keep learning

**As a developer:**

- Start with the newest Python version
- Use trivial, open data formats
- Don't boil the oceans to open a garage door (i.e. don't use an LLM if something simpler will do)
- Keep things offline if possible

_You shouldn't have to bear the burden of systemic change, but you can make the world better._

## [Climbing Out of Fixture Hell, Indirectly](https://2026.pycascades.com/program/talks/climbing-out-of-fixture-hell-indirectly/) by Sammie Jiang

Writing pytest fixtures may not scale well. Sammie's talk was a practical walk through fixture hell and how to climb out
of it using indirect parametrization.

**The test should describe _what_ it needs, not _how_ to build it.**

Fixtures describe the _how_. When you find yourself writing 14 fixtures for every combination of states (admin user,
logged-in user, user with no permissions, user with a specific subscription plan…), it's time to use indirect fixtures.

Best practices:

- Maintain test clarity
- Prefer parameter factories for complex needs
- Lazy fixture setup
- Avoid the God fixture: that one giant fixture that does too much

## [The Future of Python: Evolution or Succession?](https://2026.pycascades.com/program/talks/the-future-of-python/) by Brett Slatkin

Will Python evolve into the language everyone needs, or will it be succeeded by something else? Programming language
communities tend to migrate roughly every 30 years, and we are _overdue_. BASIC → Pascal → C → Objective-C → Swift.
JavaScript → TypeScript. Java → Kotlin.

What might Python users migrate _to_ next? Go? TypeScript? Rust? Cinder? Mojo?

He outlined what an evolved or successor Python would need:

- Better straight-line performance
- Real parallelism
- A proper type system
- Syntactic macros for expressivity (referencing [PEP 638](https://peps.python.org/pep-0638/))
- Higher level of abstraction
- Automated porting using AI tools

On macros. Brett's argument: macros let you create code that adapts to _your_ brain. Like uniquely specific words in
human languages: _saudade_, _schadenfreude_, where one word captures a concept that takes a paragraph to translate. What
if Python had that kind of expressive power baked in?

He framed two camps in AI-enabled software development:

- **Code is ephemeral** (Steve Yegge's "Gastown"): I write specs, I get working software.
- **Readability still matters** (Paul Graham's "100 Year Language"): I need high-level abstractions that precisely model
  my intention. Human language will never be good enough. Humans have to be responsible, so we need to be able to debug.

I can definitely see both. For personal projects especially, I don't care about the internals. I'm way past the learning
stage, I just need some tools that can help me. But when I'm getting paid to write and maintain software, it's a
different thing.

The opportunity Brett sees is humans co-designing language extensions while AI optimizes for human debuggability.

Will Python evolve? Will _we_?

## [Airflow Beyond the Cloud](https://2026.pycascades.com/program/talks/airflow-beyond-the-cloud/) by Constance Martineau

Constance gave one of those wonderfully over-engineered project talks I love. She ran Apache Airflow on a Raspberry Pi
Zero, to orchestrate an On-Air sign in her office so her family members wouldn't disturb her during Zoom meetings.

I love this kind of showcase project, using high-tech for your own personal needs and personal benefit. I think it is
one of the things I love about technology.

If you've followed this blog or seen my
[DjangoCon US 2025 talk](https://www.youtube.com/watch?v=7knxXLg4enA&list=PL2NFhrDSOxgUSZVGkmbMhUpaaZ1ORfpCl&index=32),
you know that I run [secretcodes.dev](https://secretcodes.dev): my own little Django app where I built a QR code
generator and a URL forwarder, an MCP agent, and an availability check.

Sometimes the work needing orchestration and automation is in a factory, a greenhouse, somewhere with no VPN, no open
ports, and a flaky internet connection.

Her design principles for constrained environments:

- Pull beats push
- No open ports, no VPN
- Simple beats clever
- _"The dumbest thing that works is the most reliable thing on stage."_

Use `pgrep` over the Zoom API. Use a flag file over Kafka. Workflows don't always live in the cloud, and that's a good
thing to remember.

## [To Notebook or Not to Notebook](https://2026.pycascades.com/program/talks/to-notebook-or-not-to-notebook/) by Rodrigo Silva Ferreira

_Nature_ named Jupyter one of the ten projects that transformed science, and there are over 10 million notebooks on
GitHub.

He acknowledged the controversies (Joel Grus's famous "I don't like notebooks" talk, the original PyData "Notebook
War"), but he made a strong case for notebooks beyond their technical aspects:

- Memory and reproducibility
- Collaboration and community
- Narrative and incremental thinking
- A bridge between computation and storytelling
- The act of playing, the playful nature of exploratory data analysis

Sometimes you're not building a pipeline, you're just _playing_ with data, and notebooks are the right environment for
that.

He pointed us toward [marketplace.orbrx.io](http://marketplace.orbrx.io) for Jupyter extensions: `jupyterlab-git`,
`ipywidgets`, `variableinspector`, `spellchecker`.

## [Getting Started with Open Source Contributions](https://2026.pycascades.com/program/talks/getting-started-with-open-source-contributions/) by Stefanie Molin

Stefanie's talk was perfect for newcomers, and a good reminder for the rest of us. She busted two myths up front:

> **Myth 1:** Only professional developers or maintainers can contribute.
>
> **Myth 2:** Only experts can contribute something meaningful.

Both wrong. **No contribution is too small.**

Her process for getting started:

1. Make a list of the projects you use or have used
2. Write it down
3. Evaluate them for suitability: software license (your employer might restrict you!), recent activity, codebase size,
   tech stack, repo access
4. Identify a way to contribute: sprints, examples in the documentation, bug reports, docs fixes, or even just checking
   if a feature has already been requested

There are really a lot of great tips from Stefanie in this talk. Sometimes you just need to show your initiative and
suggest ways to improve the project. It's not always reactive, like always waiting to be assigned an issue.

I've been in the open source community for a long time, I forgot the beginner's mindset of how to get started
contributing to open source. From now on, if anyone asked me how to get started, I would just tell them to watch
Stefanie's talk.

## [Variables and Objects in Python: It's Pointers All the Way Down](https://2026.pycascades.com/program/talks/variables-and-objects-in-python/) by Trey Hunner

Trey's talk was a clear walk through one of the trickiest mental models in Python.

Python doesn't officially call them "pointers". The docs say "binding" or "reference", but Trey prefers "pointer"
because it's like an arrow pointing to a thing. And once you have that mental model, a lot of "weird" Python behavior
becomes obvious.

The two key distinctions:

- **Assignment changes variables. Mutation changes objects.**
- **Equality is about objects. Identity is about variables.**

Subtle but important point: **data structures don't contain data, they contain references.** Copying objects takes time
and memory. Python made a tradeoff. Every language design decision is a tradeoff. _"This is bad? Compared to what?"_

Slides are at [trey.io/pycascades26](http://trey.io/pycascades26).

## My Own Talk: [No More Spreadsheets](https://2026.pycascades.com/program/talks/no-more-spreadsheets-building-pyladiescon-infrastructure-with-python-and-django/)

I also gave my own talk: No More Spreadsheets!

Did you know, even though I have been going to PyCascades for many years, (and co-founded the conference), this was the
first time I was a real speaker, by myself? (I was 1/3rd of a Speaker in 2019 giving a talk alongside Elaine Wong and
Lorena Mesa, and also a panelist in 2021 and 2024.)

Well, this was my first conference talk of the year, and the very first iteration of this version. I have previously
presented the same topic as a lightning talk at PyCon US Community Organizers Summit, and at Djangonauts Space, but I
didn't have enough time to present the topic fully. Turns out I needed a full talk length to cover this passion topic of
mine.

I'll be giving an updated and more refined version of it one more time at
[PyCon US](https://us.pycon.org/2026/schedule/presentation/80/) later this year. So if you missed it at PyCascades, come
find me there. To everyone who came to the talk, watched it, or talked to me about it afterwards, thank you. I received
so many compliments about it, and I really appreciate the kind words.

## Ice Cream Selfie

Ice cream selfie at Bella Gelateria with Mario Munoz, Trey Hunner, Stefanie Molin, Michael Nekrasov, Stuart Williams
{{<fosstodon user="mariatta" id="116271182370017629">}}

## See you at the next conference

Thanks to the PyCascades organizers, volunteers, and speakers for making this happen. Looking forward to seeing you at
some other conference!

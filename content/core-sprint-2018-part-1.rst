Python Core Sprint 2018: Part One
#################################

:date: 2018-09-15 11:20
:slug: core-sprint-2018-part-1
:category: Python
:tags: Python, sprint, miss-islington, blurb_it
:author: Mariatta


For the past week (September 9-14), I've been down in Bellevue, WA for my second
Core Python sprint. The sprint is hosted by Microsoft, and funded by The PSF.

Thanks
======

Last year, I was only able to stay for the sprint for three days. This year
I'm able to stay for the entire week. I got a lot more things done.

Thanks Steve Dower, for organizing this sprint and figuring out all the
logistics for us. Coordinating this is no easy task, and everything runs smoothly.

Big thanks to Microsoft for hosting us in Reactor Redmond B20. The facility and the
campus was really awesome. (Ice cream at the back of the room!) I got to
try out the Hololens! Thanks for treating us for a nice dinner, with guest speaker
`Anders Hejlsberg <https://en.wikipedia.org/wiki/Anders_Hejlsberg>`_.

Thanks to The PSF for providing the fund, getting many core devs from all over the
world. It's been valuable being able to spend the whole week collaborating and
talk face-to-face. We really don't get too many opportunities to do this. Sprints
at conferences are normally our opportunity to help onboard new contributors
to Python. Core sprint like this serves a different purpose where we get to focus
on some of our bigger projects, brainstorm with each other, and make decisions.

Thanks to Zapier, especially my manager, and my teammates at the Partner Engagement
Team, for being supportive and giving me the time away from work. Zapier has
flexible time off policy, so I'm not limited to only taking X days off from work
each year. In addition, I get to focus on Python for the whole week, and not
needed to keep doing daily standup or weekly team meetings.

Thanks to my family, for supporting and being able to manage themselves while
I'm away. I have been traveling away without them, for work and for Python, once
a month each month since January of this year, and even more of such trips that's
been arranged all the way until August 2019. It really has not been easy for
all of us. But it motivated me to make the most of my time at the sprint.

Thanks to the core developers who came, away from their home, from their family and work,
for Python. We had many great discussions and chats during the past week, they've
all been very productive, and I really enjoyed being able to spend time with everyone
for Python.

Daily Updates
=============

I've posted my daily updates on twitter.

Here's the copy-pasta 🍝 version:

`Day 1 <https://twitter.com/mariatta/status/1039506319676387330>`_ report:

- automerge bot
- reviewed Larry's fake f-strings hack
- CLA discussion with Brett
- #PEP581 discussion with Ezio
- helped Ethan/Carol with git
- trying to name project
- started new unnamed project
- wrote emails

`Day 2 <https://twitter.com/mariatta/status/1039742549727031304>`_ report:

- show off automerge bot
- CLA discussion with Brett
- chat about workflow, bots, #PEP581 with Kushal, Victor, Pablo, and Guido
- helped Ethan with git
- decided on new project name: blurb_it
- wrote emails

`Day 3 <https://twitter.com/mariatta/status/1040062970728837120>`_ report:

- #PEP581 group chat with Ezio, Ned, Pablo, Petr
- work on blurb_it
- core dev group chat
- small enhancement to automerge bot
- bought an xbox

`Day 4 <https://twitter.com/mariatta/status/1040433812407107584>`_ report:

- dealt with CoC case
- chat about aiohttp async task queues with Andrew
- work on blurb_it
- PSF infra chat with Ernest
- core dev group chats
- gave lightning talk about miss-islington and blurb_it at Microsoft meetup

`Day 5 <https://twitter.com/mariatta/status/1040765915518754816>`_ report:

- miss-islington rate limit issues 😕
- `self-declaration <https://github.com/python/devguide/pull/414>`_ as "interested in emoji" 😎
- Python language summit planning with Lukasz
- deployed unofficial blurb_it
- exhausted 😩
- three shots of tequila 🥃

New Python Core Developers
==========================

Welcome Emily Morehouse-Valcarcel and Lisa Roach as new Python core developers!
They're both brilliant, and have been `contributing to Python
<https://mail.python.org/pipermail/python-committers/2018-September/006059.html>`_
in the past couple years.

miss-islington
==============

miss-islington is a GitHub bot that first developed at last year's core sprint.
The original task of miss-islington was to automatically create backport PRs.

Over time, she gained new privilege. She's been allowed to merge her own PR once
it has been approved by another core dev.

This week, miss-islington gained a new superpower. She can now automatically
merge any pull requests that core dev wants her to merge.

As context, there had been long and lengthy discussion about this "automerge"
ability. Discussion started in `core-workflow issue #29 <https://github.com/python/core-workflow/issues/29>`_,
opened by Donald Stufft February 2017. It is one functionality that GitLab
has that improves productivity, that GitHub does not yet provide. And as indication
of how complicated CPython workflow is, further discussion about this spilled over to
`bedevere issue #14 <https://github.com/python/bedevere/issues/14>`_.

While we have come to the resolution and decision of `how the automerge
<https://github.com/python/bedevere/issues/14#issuecomment-399585735>`_ should
work, I guess I just have not find any time to completely focus and work
on implementing it. I spent almost the whole day of the first day of sprint
to implement this. I don't normally have that "one full day to focus and undisturbed to work on Python"
thing, so needless to say, I might never get this done without coming to the sprint.

If you're curious of how this was implemented, miss-islington is `open source <https://github.com/python/miss-islington>`_.
In addition, I will give a keynote speech at `DjangoCon US 2018 <https://2018.djangocon.us/news/mariatta-wijaya/>`_,
titled **Don't Be a Robot; Build the Bot**
where I plan to describe some of miss-islington's architecture and challenges in
building it.

These are the pull requests related to automerge feature:

- `Automerge PR labeled with "automerge" <https://github.com/python/miss-islington/pull/146>`_
- `Normalize commit messages on automerge <https://github.com/python/miss-islington/pull/151>`_
- `Don't automerge if there is "DO-NOT-MERGE" label and "CLA not signed" label <https://github.com/python/miss-islington/pull/152>`_

Open issues that we will need to address, eventually:

- `Rate limited since the automerge has been deployed. <https://github.com/python/miss-islington/issues/153>`_
- `Keep track of who triggered the automerge <https://github.com/python/miss-islington/issues/155>`_
- `Miss-islington should not self-assign PR that failed to backport <https://github.com/python/miss-islington/issues/154>`_
- `automerge shouldn't let GH wrap the first line of the commit message <https://github.com/python/miss-islington/issues/159>`_

You can also read my announcement to `python-committers <https://mail.python.org/pipermail/python-committers/2018-September/006043.html>`_ about the automerge,
as well as watch a `YouTube demo video <https://youtu.be/p85YtKKLNno>`_.


Blurb it!
=========

Part of our requirement for every pull requests that you send to CPython, is a news
entry describing the change. This had been heavily discussed and designed in
`core-workflow issue #6 <https://github.com/python/core-workflow/issues/6>`_,
and we now have Larry Hasting's tool, `blurb <https://pypi.org/project/blurb/>`_
(available on PyPI), to help with this. In addition, we have a status check in place
by `bedevere <https://github.com/python/bedevere>`_ to ensure that the news
file exists, and that we don't forget to add it.

Larry's blurb works really great, and everyone has been using it without issues.

My personal nitpick about this, is that (and it's because I'm very lazy), blurb
is a command line tool, and so I have to be on my computer in order to use it.
A lot of time, I found myself reviewing a pull request while on my phone,
and all it needed was a news entry. But since I was on my phone, on transit,
by the beach, or whatever, I could not complete this process, and had to
wait until I'm back on the computer.

So I've been thinking that it would be nice and convenient if there was a web
interface for blurb. A place for me to fill in a form, and the news file automatically
gets added to the pull request. I had asked Larry earlier at PyCon what he thinks
about this idea. He said that he's okay with it, and he had in fact `mentioned it himself
<https://mail.python.org/pipermail/python-dev/2017-June/148448.html>`_: *"... it should be easy for
some JavaScript expert to write a static page that generates blurb files
for you--it provides a form, you fill it out, and you "download" the
blurb file.  (I've seen pages that do that sort of thing, though I don't
know how to write that kind of JavaScript myself.)"* (python-dev, June 24, 2017).

Since I don't actually know how to write that kind of JavaScript either, I wrote
it all in Python 3.7, using fine libraries like `aiohttp
<https://aiohttp.readthedocs.io/en/latest/>`_, `aiohttp-session
<https://aiohttp-session.readthedocs.io/en/latest/>`_,
`aiohttp-jinja2 <https://aiohttp-jinja2.readthedocs.io/en/stable/>`_, asyncio, and
`gidgethub <https://gidgethub.readthedocs.io/en/latest/>`_.

Before starting to write this project, I needed to come up with a project name,
and of course it was the hardest part of the process. I had thought of unimaginative
names like, "Blurb on the web" or "blurb_ee (ee: extended edition, pronounced *blurbee*)".
Eric V. Smith suggested "Blurb 2.0". It sounds okay, except that I'm not actually implementing
a new "blurb". I'm trying to provide an enhancement of "blurb add" command, so it
is only a subset of the full "blurb". "Blurb 2.0" sounds incorrect to me. Larry
himself suggested: "webLurb" (pronounced webblurb, or maybe we blurb?). In the end,
I went with, "blurb_it", to which Guido responded: "ship_it". 🚢

I demoed the prototype of blurb_it at Microsoft meetup on Thursday. I've started
a `pull request <https://github.com/python/blurb_it/pull/2>`_, and currently
it is available on my own free Heroku instance at https://my-blurb-it.herokuapp.com/

There are still more work to be done for blurb_it:

- Write unit tests
- Add travis CI integration to the repo
- Transfer app ownership to The PSF
- Make it as a GitHub App instead of an OAuth App
- Add form validation that the news entry has to be more than 30 characters
- Ask for Andrew's feedback on best practises when using aiohttp-session


To be continued
===============

That is all the time I have to write up about the sprint. I'm heading back to
Vancouver, and will be out-of-open source for the rest of the month. But I plan
to continue with more details of some of the other projects.

Thanks for reading.
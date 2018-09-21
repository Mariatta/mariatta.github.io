Python Core Sprint 2018: Part Two
#################################

:slug: core-sprint-2018-part-2
:category: Python
:tags: Python, sprint, cla, pep581
:author: Mariatta


Read up on `Part one <https://mariatta.ca/core-sprint-2018-part-1.html>`_ first.

Here are additional discussions and projects that I got involved with during the
sprint.

PEP 581
=======

`PEP 581 <https://www.python.org/dev/peps/pep-0581/>`_ is a PEP I wrote about using
GitHub issues instead of Roundup as CPython's issue tracker.

During the sprint, I discussed this topic mainly with Ezio Melotti, as well as
with a group of other core devs: Ned Deily, Kushal Das, Petr Viktorin, Pablo Galindo,
and one-on-one with Zachary Ware.

Thanks all of you who came and discussed this with me, I really appreciate your
input and feedback.

Reflecting back, my tone might have been unkind, impatient, and unempathetic during
certain parts of the group discussion, and I'm sorry.

Unlike most other PEPs, the idea for this PEP did not go through rounds of
discussions over at python-ideas. And unlike other PEPs, I did not post this PEP
into python-dev after it has been written. It was my own choice. Instead, this idea
was discussed at Python Language Summit, as a thread at python-committers, and
I also chatted privately with a few other Python core developers.

Ezio, who maintains Roundup for CPython, talked to various core devs individually
to get a sense whether people are warm to the idea of moving to GitHub. It seems
like people are postive about it, or at least not strongly opposing the idea,  but
we still need to iron out additional details.

These are some of the concerns raised during the discussions with core devs at
the sprint:

**What if GitHub disappear suddenly?**

I realize that my response to this question had been unkind, impatient,
unempathetic, and I'm sorry.

My response was *"I don't care"*.

What I really meant is, *"I don't believe GitHub will go away all that suddenly"*,
and that is my personal opinion, and I know there are people who thinks otherwise,
and I respect the difference in opinion.

But the actual question needing actual answer is: *"What is our fail safe plan?"*.
This is something that the PEP needs to address. At the moment, we'll just going to get
daily backups of GitHub data. But eventually we will need a more concrete
plan and we will need to be able to easily spin up another issue tracker / repository
so Python world does not stop and people can continue
contributing and developing.

However, this problem is not unique to CPython. Lack of fail-safe solution should
not blocking the PEP's acceptance, and should not stop us from using GitHub issues.

**What about current bug triage permission?**

With Roundup currently, we have a separate "bug triage" permission that is different
than the core developer / commit access. The bug triage permission allows them
to close and categorize issues on the issue tracker, but does not give the
permission to commit or merge pull requests to CPython.

The bug triage permission is definitely valuable for the team. Historically,
we've been able to give this permission easily to people without much formality,
whereas giving commit access is not so trivial.

We definitely need bug triage help, and the question is, how will this be managed
with GitHub?

There are a couple ideas. Donald Stufft commented in Zulip that we can give
people write access, invite them as team collaborators, this will allow them to
edit and close issues, but use the GitHub branch protection feature to restrict
pushing codes to only Python core developers. BTW, we have been using this
feature, just didn't quite realize it. Python ``3.4`` and ``3.5`` branches on GitHub
are currently "protected", and only the release manager, Larry Hastings, can
push codes to those branches.

So what we can do is to invite the current bug triagers as collaborators for
CPython repository, give them that write access, and add branch protection
such that only Python core developers can push / commit into the active branches.

Another idea that came up while chatting with Zach, now that miss-islington
can automerge, maybe we let only miss-islington to merge and commit from now on.

🤔


**The Nosy list**

Steve Dower commented that one nice feature of the existing issue tracker is
the nosy list, where he can get notified only in issues he's interested in. For
example, if someone creates an issue with "Windows" component in the current issue
tracker, he and Zach will be automatically notified and added to the nosy list.

There is not yet similar functionality on GitHub. So we're going to build out a
bot that does this somehow.

I have started researching GitHub's `notification and subscription APIs
<https://developer.github.com/v3/activity/notifications/>`_, but I don't have
clear idea or solution to this problem yet.

**Involve the Python Release manager in the transition**

Ned Deily, Release Manager for Python 3.6 and 3.7, reminded us that we will need
to include the release managers for any changes in our workflow and issue tracker.

✅

**GitHub can lower the barrier to contribute, but also makes it easier for people to submit unrelevant issues**

Some core devs were concerned that the ease of using GitHub can also mean easier
for people to use and abuse it for things other than discussing bugs and features of
Python. It means that we will need to spend more time into triaging issues, marking
things as off topic, duplicate, telling people to file their issue somewhere else,
and so on. I think this is a valid concern. But I think this is an existing problem
anyway, regardless of what issue tracker we use.

I have been experimenting with `GitMate.io <http://gitmate.io/>`_ myself.
One of Gitmate's ability is to identify if an issue is a duplicate of other previously
reported issues. GitMate is currently installed in devguide, core-workflow, and
miss-islington repos. I've seen it help several people, but sometimes it is not
so helpful.


**CoC enforcement**

We need to have better and clearer policy on CoC enforcement for handling comments
on GitHub. I know that there is the PSF's CoC work group now, and Brett is part of that
group. I'm glad that there is some progress, and I look forward hearing more from the
CoC work group.


CLA
===

Another aspect of CPython's workflow that could use an improvement is the way we
handle CLA (Contributor License Agreement).

The way it works, for every contribution and pull request you made to Python
(CPython, DevGuide, PEPs, core-workflow, and all the bots), you'll need to
sign the CLA before we can accept and merge the pull request.

There are currently several problems with this workflow:

- Signing the CLA also requires creating an account in the bug tracker. So
  people making pull requests on GitHub needs to go to bugs.python.org, create
  an account, and then add in their GitHub username. While this makes sense
  for contributors to CPython, there is really no reason for contributors to
  DevGuide or cherry-picker to do this. It just slows down the process of
  contributing.

- It requires manual work by members of The PSF (Ewa and Betsy) to check if the CLA
  has been signed, and they have to manually update the record in bugs.python.org.

- After the CLA has been signed, the pull request does not get automatically
  updated with this new information. Contributors used to have to ping a core
  developer to update the label on the PR, and a core developer has to come back
  to the PR and remove the label. This has gotten better recently, with the
  `check-python-cla <https://check-python-cla.herokuapp.com/>`_ website. But it
  still is somewhat manual process.

- It could take at least a day, sometimes more, for the CLA process to clear. It
  blocks pull requests from being merged.

It really would be nice if this whole process can be automated, not requires much
human involvement, and if it can be completed in seconds instead of days.

I've been discussing this issue with Brett since early this year. I've also
started a `couple threads <https://mail.python.org/mm3/archives/list/core-workflow@python.org/thread/JBV3XJVD2DLDX5DY7TZEA6CO5YPNHJ2C/>`_
in core-workflow mailing list. Per Yury's suggestion, I've started looking into
`cla-assistant <https://cla-assistant.io/>`_.

During the sprint, I got to discuss this more with Brett on how to proceed.

My personal preference is actually use the hosted version of cla-assistant,
so we don't have to maintain it. (**We** here really means only myself, Brett,
and Ernest).

People expressed concern that the system could go away quite suddenly, so
we're going to need to have some fail-safe mechanism if that ever happens.

I think the problem of "what if this goes away suddenly" is not be unique problem
to Python. I'm now actually curious to hear from other projects that use hosted
cla-assistant, and if they have their own backup plan in place.

I chatted with Ernest, and he said it will be easy enough for us to host our
own instance of CLA assistant. Ernest has started looking into it.

Several outstanding issues with cla-assistant:

- How does it handle people who signed on behalf of an organization?

- It allows us to `request more information from the CLA signer
  <https://github.com/cla-assistant/cla-assistant#request-more-information-from-the-cla-signer>`_,
  but when we export the data, the additional metada were not returned. It seems
  like a bug.

- How do we get daily backups automatically? It seems like the only way to get the
  backup is by going to the website, and click on a menu item that says "Export".
  Is there an API endpoint we can use, or do we need to build it ourselves?

- How do we export out current signed CLAs from the bug tracker to cla-assistant?
  Ezio had actually started working on getting me a ``.csv`` for it.

I ran out of time and energy to follow through with all of the above during the
sprint, so sadly we're still not yet using this new system.

Thanks Brett, Ernest, and Ezio for looking into this with me.


Fake f-strings
==============

I selfishly wanted Larry to `drop Python 3.5 support
<https://github.com/python/core-workflow/issues/283>`_ in blurb. Blurb was
initially written with f-strings, but later on, all f-strings were replaced with
`str.format <https://github.com/python/core-workflow/pull/146>`_.

I've been quite disappointed about it since last year, and I know I actually
have better things to do than being sad about a tool so crucial for CPython does
not have any f-strings in it.

Anyways, Larry entertained my selfish request and came up with `fake f-strings
<https://github.com/python/core-workflow/pull/288>`_.

I'll take it. Thanks Larry.


Real f-strings and asyncio
==========================

Up until the sprint, I had never tried doing something like ``f"{await somecoroutine()}"``,
so I didn't know if it would even work. Since the creators and maintainers of
f-strings and asyncio are in the room, I thought I'll just ask them if it can work,
and I should get a quick firm "yes/no" answer.

There was slight hesitation from core devs in answering such question.

*"It should work?"*

*"I think so?"*

So Brett wrote us a small script to see if it will really work, with myself and
Eric V. Smith as witness. The result is, this works for Python 3.7+.

I found out later that it does not work in Python 3.6, but I don't actually know
the reason why. Something changed with how ``await`` works between 3.6 and 3.7?

🤷🏻‍♀


**Update:** Yury `commented on twitter <https://twitter.com/1st1/status/1042858310641152001>`_:
*"yes, this needs Python 3.7+ to work. Before 3.7 async and await were not proper
keywords, so the interpreter did not recognize them in some contexts."*

Thanks Yury! Now we have new reason to start using Python 3.7+!


To be continued
===============

There will be Part 3, *someday*.


Thanks for reading.
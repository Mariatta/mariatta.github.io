Weekly Update, Feb 16, 2019
###########################

:date: 2019-02-16 11:00
:category: weekly-updates
:author: Mariatta


This is the first of my Weekly Updates post. `Background on this topic. <../pages/weekly-updates.html>`_.
I'll try my best to keep this up.

PyCascades
----------

- Entering the last two weeks before the conference. Lots of little details still being sorted out.

- Worked on the `welcome wagon <https://pycascades-welcome-wagon-2019.readthedocs.io/en/latest/>`_.
  Lots of updates to the travel guide and dining guide.

- Considered using a different theme than alabaster for the welcome wagon. There's
  a PR with a new theme, and it's looking great. But I felt somewhat uncomfortable
  to switch to another theme that doesn't support Read The Docs' ethical advertisement.
  I recommended PyCascades to support RTD some other way if we're going to not
  use the theme anymore.

- The entire team has continued to working tirelessly. Being a remote organizer,
  sometimes I feel like I'm just the "Chief Nagging Officer", keep asking them about
  things, and not actually able to do anything. So all I can do is cheer.

- We finally secured a sprint venue. I updated the welcome wagon with
  `sprint info <https://pycascades-welcome-wagon-2019.readthedocs.io/en/latest/sprint.html>`_,
  and added `registration ticket <https://ti.to/pycascades/pycascades-2019/with/senvon2fuek>`_.

- Huddled with the CoC committee.

- An attendee raised a concern about our venue accessibility. Discussed with Maelle
  and Thea. We updated the Accessibility page with a `fragrance free consideration <https://2019.pycascades.com/accessibility/>`_ section.

Core Python Workflow
--------------------

- Ned Deily pinged me about an issue with bedevere's "check News" status. It wasn't
  working the way we liked, and was blocking a PR from `getting merged <https://github.com/python/cpython/pull/11779#issuecomment-462498706>`_.
  So I made a `PR to quickly fix it <https://github.com/python/bedevere/pull/152>`_.

- While working on that issue, I realized that the GitHub bots have not been tested
  against the latest Python versions, due to `known issue in Travis CI <https://github.com/travis-ci/travis-ci/issues/9069>`_.
  We have been testing against Python 3.7.0a4, and we weren't even testing against
  Python 3.8. So I went ahead and adjusted the travis configuration files and made
  sure they're tested against 3.7.2 and 3.8.0. If you're curious,
  `here's an example of how to configure Travis CI to test against the latest Python versions <https://github.com/python/bedevere/blob/5bb398ed02be63b461551fdfe365eb9e090053a3/.travis.yml>`_.

- One thing lead to another. Now tests are passing in Python 3.7.2 but failing in
  3.8.0. We're not sure if the regression is with ``aiohttp`` (3rd party library)
  or ``asyncio`` (Core Python). Currently waiting for `Andrew to investigate <https://github.com/aio-libs/aiohttp/issues/3606>`_.

- Asked in Python committers on how to proceed with `PEP 581 <https://discuss.python.org/t/what-are-next-steps-for-pep-581/>`_.

- Merged several PRs.

- Set up netlify to `preview pull requests in Devguide <https://github.com/python/devguide/issues/463>`_.

PyCon
-----

- Got news that my talk has been accepted! Happy to reprise my talk, "Don't Be a
  Robot; Build the Bot".

- Booked my flights and hotel. I'm going to arrive on Monday, April 29 (11 PM or
  so). I'm hoping that'll give me to adjust to jet lag (yeah I know.. I'm old)
  and a lot of time in case I need to chat with Łukasz about the language summit,
  or with Andrew about our tutorial.

Mentored Sprint at PyCon
------------------------

- The `Mentored Sprint at PyCon <https://us.pycon.org/2019/hatchery/mentoredsprints/>`_
  was announced last weekend. Thank you Tania, Nina,
  and Nikoleta for working together and including me into this effort.

- Sign up forms are now live. Now it's time to start promote the event and get more
  signups. I've `posted to Python core developers <https://discuss.python.org/t/action-needed-participate-in-mentored-sprint-at-pycon-us/868>`_
  that I would like for them to sign up and mentor. Thank you core developers for
  committing to mentor!

- At the moment, we have a number of contributors signing up, but no projects other
  than core Python has signed up yet. Our team are now discussing strategies to
  promote and reach out to more audience.

etc.
----

- Baked brownies for kids' Valentine day school party

- Schools were closed because of the snow! Not a big deal since I work from home.
  So I have two little "interns" working with me.

- Wrote a really large check to pay for my own self-employed income tax to CRA.
  Feels good to be able to do it!

- A fun topic arised in PyLadies Slack, about debugging with 1/0 in Python. This
  is something I learned from Ned Batchelder's talk, `Machete-Mode Debugging <https://nedbatchelder.com/text/machete.html>`_.
  Sometimes you just want to test and debug, and see if your code is running and
  reached the part that you want it to reach. There are several ways to do this.
  You can raise Exception, you can add things like print("here it is"), you can
  write a nittest, you can even write to log file. But those aren't as simple as
  typing out mere 3 characters: 1/0. This for sure will cause your program to
  stop (because nobody ever really tries to catch the ``ZeroDivisionError``) and bonus,
  you get full stack trace. Now you're debugging! Of course NSFP: Not Safe for
  Production 😛).

- Last month, a kind Pythonista (who had read my `interview in RealPython <https://realpython.com/interview-mariatta-wijaya/>`_) sent me
  paypal payment, for me to spend it on ice cream. I've just gotten around buying
  a tub of Matcha Ice cream from T&T Supermarket. I haven't had this in a long
  while! It's so good! 😋

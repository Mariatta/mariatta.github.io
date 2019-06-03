Weekly Update, June 3, 2019
#############################

:date: 2019-06-03 00:00
:category: weekly-updates
:author: Mariatta

It's been a little more than two weeks since my last `weekly update <../weekly-update-may-17-2019.html>`_ 😬
Lots of things happened, and I've kept busy 😥

I spent a week in Berlin for GitHub Satellite. I might write a post just about
that later on.

Work
----

- Worked remotely from Germany for a week.

- Finished several new stories and deployed to production. Created a new API
  endpoint, built with Django Rest Framework.


Python and the community
------------------------

- Chatted with Devon Zuegel and GitHub about GitHub Sponsors program. Spent time
  creating my sponsorship tiers. I'm one of the first few maintainers with access
  to this program. You can `sponsor me on GitHub <https://github.com/users/Mariatta/sponsorship>`_
  for 5$/month.

- Listed all my current sponsors `on my personal website <https://mariatta.ca/pages/about.html>`_.

- I appeared in `GitHub Maintainer Spotlight <https://github.blog/2019-05-31-maintainer-spotlight-mariatta-wijaya/>`_.

- Blog post about `PEP 581 at Python Language Summit <https://pyfound.blogspot.com/2019/05/mariatta-wijaya-lets-use-github-issues.html>`_
  is now up.

- While in Berlin, I got to meet other Germany-based Python core developers: Christian
  Heimes, Stefan Behnel, and Matthias Klose. I also got to hang out with Raphael
  Pierzina, Jannis Leidel, other Python package maintainers, and with the scientists behind
  the historic black hole image! 🤩

  .. image:: https://pbs.twimg.com/media/D7PGneKXYAEPY-o.jpg
       :width: 400

  .. image:: https://pbs.twimg.com/media/D7djWqMUEAE6_Fh.jpg
       :width: 400

  .. image:: https://pbs.twimg.com/media/D7P7KDJXYAAH2vw.jpg
       :width: 400

- Chatted with Anwesha Das about PyLadies, and about CLA. Anwesha has a very
  interesting idea related to CLA. I won't say much about this for now until
  she has more time to research the topic and present it to the community.

- Started working on aiohttp-bot for autobackporting aiohttp pull requests. Chatted
  more with Andrew to find out his requirements for this bot. I'll probably
  have this bot ready by end of the week.

- Made several small-ish pull requests to aio-libs: `aio-redis PR #600 <https://github.com/aio-libs/aioredis/pull/600>`_,
  `.github PR #3 <https://github.com/aio-libs/.github/pull/3>`_, `aiohttp-session PR #371 <https://github.com/aio-libs/aiohttp-session/pull/371>`_,
  `aiohttp-session PR #370 <https://github.com/aio-libs/aiohttp-session/pull/370>`_.

- Some fixes to miss-islington: `PR #237 <https://github.com/python/miss-islington/pull/237>`_, `PR #234 <https://github.com/python/miss-islington/pull/234>`_.

- Released `cherry_picker v1.3.2 <https://pypi.org/project/cherry-picker/1.3.2/>`_.

- Added dependabot to my personal projects, and `to several projects under Python org <https://github.com/python/core-workflow/issues/326>`_.
  Requested the automerge to be enabled for Python.

- Started `moving cherry-picker out of core-workflow repo <https://github.com/python/core-workflow/issues/329>`_.

- `Chatted with Matthias Bussonnier <https://github.com/python/core-workflow/issues/325>`_
  about security issue with "🤖 automerge". I need to think more on how to solve this issue. 😟

- Finally got around sending out feedback forms for mentored sprint for
  diverse beginners.

- Chatted with Ernest about several infrastructure-related issues:

  * `CLA Assistant for Python <https://discuss.python.org/t/using-cla-assistant-for-python/990>`_,
    this is pending further discussion with Van Lindberg.

  * `GitHub backup data <https://github.com/python/core-workflow/issues/20>`_.
    We already have daily backup in place, it needs
    to be documented in devguide. Ernest said he will prepare the PR
    for it.

  * `Adding Sentry for CPython bots <https://discuss.python.org/t/add-sentry-integration-to-all-the-bots/1637/2>`_

- It is my turn to look after info@pyladies.com mailbox. Answered several emails,
  and forwarded emails to local chapters.

- I joined The PSF Board member's slack to get an idea what's involved as a
  board member for The PSF. After thinking more about it, I decided not to run
  for it this time. I wanted to focus on my other projects and priorities for now.

- Made a last-minute `PyLadies Vancouver meetup <https://www.meetup.com/PyLadies-Vancouver/events/261900321/>`_
  planning. I learned that Raphael will be in town, and I think it would be a
  great opportunity for PyLadies Vancouver community to meet and learn about
  pytest and cookiecutter from one of the maintainers. I'm happy that Raphael
  has kindly agreed to give a talk, but from organizers point of view, it would
  be better if we can find more speakers from our own community. It seemed
  impossible at first, but in short period of time, we're able to find
  3 additional speakers 🎉 It'll be a great Talk Night this coming Wednesday!


etc
---

- I tried currywurst in Berlin. The first one was from a food court nearby
  my hotel, and it was ... very interesting. Then Matthias took us to another
  currywurst place, Curry 36, and it was pretty good!

- Went sightseeing in Hamburg.

  .. image:: https://instagram.fyvr4-1.fna.fbcdn.net/vp/94cd1bf03e8e3fcdb3f3e2a796296576/5D8D9D11/t51.2885-15/sh0.08/e35/p640x640/60774705_842977589421413_4344408118954462167_n.jpg?_nc_ht=instagram.fyvr4-1.fna.fbcdn.net
       :width: 400

- Right after I returned from Germany, it was my husband's turn for work travel. So
  last week I was a busy single mom. It was one reason I didn't find time
  to write up my update (and jet-lagged 😵)

- Returned several times to our old home for more repairs and cleaning.
  Painters came, and the place is looking nice and fresh. I highly
  recommend hiring Liz from `Interior Paint Oasis <https://paintoasis.ca/>`_
  for your next paint job in Greater Vancouver area.

- Talked to our realtor and preparing the house to be listed. Photographers
  will come tomorrow for pictures, and the listing should be up soon after.

- It was my oldest son's birthday in the weekend. When we asked what he wants.
  he said "steak!" 😅 So we got some steak from our favorite butcher, Kea's Meats and
  Deli in Burnaby, and fired our BBQ. 🥩

  .. image:: https://instagram.fyvr4-1.fna.fbcdn.net/vp/4eb7cecd42ba68bc431d5450f994c9d1/5D963FAD/t51.2885-15/sh0.08/e35/s750x750/61717698_201827660796960_1872409219047849938_n.jpg?_nc_ht=instagram.fyvr4-1.fna.fbcdn.net
      :width: 400


Mariatta @ PyCon 2019 Recap
###########################

:date: 2019-05-15 00:00
:category: Python
:tags: Python, conference, PyCon, pep581
:author: Mariatta

I was at PyCon from April 29 - May 7. It's my fifth PyCon US. It's been a memorable
and, I kept busy.

.. image:: https://pbs.twimg.com/media/D5fCBZxXsAAnVU3.jpg
    :width: 400

I had a number of pre-planned activities for PyCon, like running the language
summit, giving talks, tutorial, etc. Thought I'll share a quick summary of how
they all went.

Zapier @ PyCon 2019
-------------------

.. image:: https://pbs.twimg.com/media/D52HmedWsAAr3D2.jpg:medium
    :width: 400

I'm one of 14 Zapiens at PyCon 2019. I staffed Zapier's booth on Friday and Saturday.
We had socks!

Python Language Summit 2019
---------------------------

The language summit was a success. First of all, we were able to stay somewhat
on time, which I'm personally quite happy about. Other thing to be proud of,
it was the most diverse audience I've seen. Our audience consists of, not just long-time
Python core developers, but also new contributors as well as members from
the wider Python ecosystem, such as from Twisted, Django, and BeeWare project.
We had talks about circuit Python, team communication, and mentorship. I personally
think all the talks were very interesting and refreshing.

We've invited A. Jesse Jiryu Davis to cover the event. You can see his posts
at The PSF's `official blog <http://pyfound.blogspot.com/2019/05/the-2019-python-language-summit.html>`_.

We forgot to take a group photo after the summit!! 😱 but we had a group photo
with PyCon staff ... (image from `PyCon's twitter account <https://twitter.com/pystar/status/1123782745585483776>`_)

.. image:: https://pbs.twimg.com/media/D5hQscyW0AEIjUs.jpg


PEP 581
-------

One of the topic of discussion was `PEP 581 <https://www.python.org/dev/peps/pep-0581/>`_. Since Jesse is writing up the
post about it, I won't duplicate the effort. But you can see `my slides here <https://speakerdeck.com/mariatta/pep-581>`_.

I'd really like to see us making progress with this before the next Python
Language Summit. There were lots of action items, and things we still need
to figure out, but those will be addressed in `PEP 588 <https://www.python.org/dev/peps/pep-0588/>`_.

I plan to update PEP 588 with the items raised during the language summit,
I really haven't had much time to do this.

Hands-on Intro to aiohttp
-------------------------

Andrew Svetlov and I gave a `beginner tutorial to aiohttp <https://us-pycon-2019-tutorial.readthedocs.io/>`_.
Our tutorial material is available online, and licensed under CC-BY-SA 4.0.

Andrew is the maintainer of `aiohttp <https://docs.aiohttp.org/en/stable/>`_, which
is licensed under Apache 2.0, He's very knowledgeable about it.
There were lots of interesting questions being asked at the tutorial, and he was
able to explain things clearly. `Stéphane Wirtel <https://twitter.com/matrixise>`_
and `Sviatoslav Sydorenko <https://twitter.com/webKnjaZ>`_ volunteered as our TA.

.. image:: https://pbs.twimg.com/media/D56v23uWAAIfE2Q.jpg
    :width: 400

Don't Be a Robot; Build the Bot
-------------------------------

Friday after the keynote, I gave my talk titled `Don't Be a Robot; Build the Bot
<https://www.youtube.com/watch?v=_xdEAxLuj9Y>`_.
I loved giving that talk! It's a talk about `miss-islington
<https://github.com/python/miss-islington/>`_!
I think more people should be building their own bots and automate! With
`gidgethub <https://gidgethub.readthedocs.io/en/latest/>`_ (Apache 2.0 licensed)
it is really easy.

GitHub bots are one honking great idea, let's do more of those!
---------------------------------------------------------------

Sviatoslav and I hosted an open space on Sunday. We discussed more about GitHub bots,
building it for profit or for fun. Sviatoslav just made a new framework for building
GitHub Apps with Python 3.7, called `octomachinery <https://octomachinery.dev/>`_.
We also discussed about GitHub Actions, tried to make sense of it, e.g. what were
limitations, and what Actions would be useful. There is a `proposal
<https://discuss.python.org/t/official-github-action-for-publishing-to-pypi/1061>`_
for making an "official" GitHub Action for publishing to PyPI. Some people shared
ideas of what bots they'd like to see and build.

One attendee (I think his name was Anurag Saxena(?)) said he'd like to
receive weekly updates of GitHub issues/PRs they
worked on, and to have it automatically sent to him as email or slack or
something. I think this is very interesting idea.

Product placement: this can be accomplished with Zapier. You can create a
cron job that generates the summary (by utilizing GitHub Search API), and then use
`Webhook by Zapier <https://zapier.com/apps/webhook/integrations>`_ to handle the
"send email/post a slack message".

Status of black-out
-------------------

I mentioned my personal bot, `black-out <https://github.com/mariatta/black_out>`_, in
my talk. Black-out is a GitHub bot that runs black (Python formatter) on incoming pull
requests. The first version of the webhook-based bot is open source and Apache 2.0
licensed. However, I wasn't happy with how it works, so I've been researching on
how to turn it into a GitHub App.

I've made some progress with black-out GitHub App, I've implemented some of the features
I wanted for myself, but I'm still just experimenting and testing it out on my
own personal projects to really figure out what's the best workflow for the bot.

Black-out GitHub App is still closed source, I have not put it up on GitHub yet.
After the talk, a few people, including `Jannis Leidel <https://twitter.com/jezdez>`_
from Mozilla, expressed interest in black-out, and wanted to know how they can help.

Thanks for the interest! I think I just need to find time and put it up on GitHub
so we can all collaborate!

aiohttp bot
-----------

aiohttp needs a bot just like miss-islington, for backporting, and Andrew Svetlov
had talked to me about this since early last year. (and Ansible needs their own
backport bot too). To help with this, we've been working to make `cherry-picker.py
<https://pypi.org/project/cherry-picker/>`_ customizable. I've offered to help
build this bot for aiohttp, and the easiest is a webhook-based bot, just like
miss-islington. However Sviatoslav disagrees. He prefers for it to be a GitHub
App that can be easily installed by other projects. While I like the GitHub App
idea, for reusability, I also think that each projects might have different workflow
for backporting, so we'll end up having to support "configuring the bot", which is
a boring activity for me. I'll be thinking more about this, but my thinking right
now is to build it as a personal bot for aiohttp; not a customizable bot.

Mentored Sprint for Diverse Beginners
-------------------------------------

On Saturday afternoon (4 hrs) I helped ran the mentored sprint for Diverse Beginners. This
is a group effort with Tania Allard, Nina Zakharenko, and Nikoleta Glynatsi. We have
a room full of 70 new aspiring open source contributors, and about 30 mentors
from 11 different open source projects (like CPython, CircuitPython, TensorFlow,
etc) I think it was great success! The projects and mentors were tasked with
coming up with at least 5 beginner friendly issues, so they came prepared. Lots
of people with diverse background made their first pull requests at the sprint.

Another thing that surprised me, was such great turnout! I've organized lots of
events and meetups, and we usually expect about 60% people will actually show up.
But for this event, **EVERYBODY** showed up! Room was completely full!! (103 pax capacity)
We even had to turn away many people who wanted to walk-in.

.. image:: https://photos.app.goo.gl/YRJD9tkQSHZBzFcB9
    :width: 400


Keynotes
--------

I managed to see pretty much all of the keynotes, except for Jessica McKellar's keynote.
Her keynote started late, and I was supposed to staff Zapier's booth at the same
time.

Sha's talk was very inspiring and emotional. I'm glad I was able to watch the
talk in person. I was going to suggest people to catch his talk, but unfortunately
there was no recording.

I also enjoyed the `Steering council plenary session <https://youtu.be/8dDp-UHBJ_A>`_
moderated by Ewa Jodlowska. (there was mention about PEP 581!!)

PyCascades
----------

.. image:: https://pbs.twimg.com/media/D50oSeaXkAEb-uv.jpg:large
    :width: 400

On Sunday I met up with several PyCascades organizers and we discussed the planning of
next year's conference. We're still scouting venues in Portland, and figuring out
how to best divide tasks among the organizers. Eric Holscher will be co-chairing,
along with Esti. Somehow during that meeting, I became the next PyCascades
Diversity Chair.

PyLadies
--------

.. image:: https://pbs.twimg.com/media/D56C8oTX4AESrtq.jpg:large
    :width: 400

(image from `Lorena Mesa on Twitter <https://twitter.com/loooorenanicole/status/1125485680216485888>`_).

On Monday I attended a meeting with other PyLadies organizers from all over the world.
We shared notes about organizing and leading our own local chapters. We learned that
the challenges faced by PyLadies in different parts of the world are different. We
talked about how the current representation of PyLadies isn't very diverse (represented
by people in North America) whereas members of Python community and PyLadies are coming
from all over the world. We talked about ideas on how PyLadies can be better. We
discussed the governance of PyLadies, and decided to do a monthly PyLadies organizers
meeting. Elaine and I volunteered to take over managing info at pyladies email.

DEP 9
-----

I ran into Andrew Godwin who is a Django Core Developer. I got to ask him about
Django and asyncio. During the aiohttp tutorial, someone had asked about aiohttp
and ORM. Andrew Svetlov mentioned that it is a low priority for aiohttp, and so
I wondered what is Django's stance on this. Andrew (Godwin) shared his plan about
async-capable django. I guess he was talking about `DEP 9 <https://twitter.com/andrewgodwin/status/1126328701593866240>`_.

Language Summit retro, and the inspiration for black
----------------------------------------------------

I met with Łukasz Langa to celebrate success of running our first language summit.
We had informal retros, and started thinking about how to put the next year's event.

I also got to ask him where the inspiration for black came from. He described
frustration with other auto-formatter, how it does not provide consistent
output (same file reformatted twice would give different result). After months
of frustration, he decided to make his own auto-formatter.

.. image:: https://pbs.twimg.com/media/D55tCx_W0AAT3tF.jpg
    :width: 400


F-string Debug Mode
-------------------

Of course I had to give away all of my new f-string stickers to Eric V. Smith.

Eric showed me a demo of debug mode for f-string. It adds the `=` to the f-string
expression. I recalled we had this discussion with both Eric and Larry Hastings back during core Python sprint.

It works like this::

    foo=5 print(f"{foo=}")


would print::

    foo=5

Since then the PR has been merged, and now we need to `write the documentation <https://bugs.python.org/issue36858>`_.


.. image:: https://pbs.twimg.com/media/D551XvfW4AImG49.jpg
    :width: 400

People
------

I finally got to meet in person with people I've interacted online a lot, like:
Tania Allard, Cheryl Sabella, Anthony Shaw, Sviatoslav Sydorenko, Elizaaveta Shashkova,
and many more!

.. image:: https://pbs.twimg.com/media/D56eogZW0AAUZat.jpg
    :width: 400

CoC Incidents
-------------

During the conference, it was brought to my attention about several CoC incidents
that occurred in various communities I belong to. These issues are being dealt
with, and I've also talked to PyCon incident response team members where appropriate.


Ice Cream Selfie
----------------

I had ice cream sandwich from Cathy's Gourmet Ice Cream Sandwiches, courtesy of Tania and Nina 🍨😝🤳🏻

.. image:: https://pbs.twimg.com/media/D568l3_WsAE3pF7.jpg:large
    :width: 400


PyNutella
---------

PyNutella, a.k.a that thing where Mariatta asks her friends who are coming to
PyCon to bring her Nutella from Europe, yeah that happened. Thanks to Christian
Heimes for the very special Nutella. My kids were mind blown to see them. Also
thanks to Stéphane Wirtel for a really big jar of Nutella from Belgium.

.. image:: https://pbs.twimg.com/media/D5l36DKW4AAsgKP.jpg
    :width: 400


PierogiCon
----------

Anna Ossowski, Jeff Triplett and I went back to Sokolowski's University Inn for the
second PierogiCon, and we brought in a number of newbies.

.. image:: https://instagram.fyvr4-1.fna.fbcdn.net/vp/d67f75c6b92d5fe66cb81e3dc124e539/5D660D3C/t51.2885-15/sh0.08/e35/s640x640/59183211_108900943546171_9078212037958768043_n.jpg?_nc_ht=instagram.fyvr4-1.fna.fbcdn.net
    :width: 400

Selfie Sprint
-------------

I was meaning to do one day of sprints, but after a full week full of activities,
I decided not to do any open source activities, and instead just go around
and `take selfie with people I met <https://twitter.com/search?f=tweets&vertical=default&q=mariatta%20%23selfiesprint&src=typd>`_.

I enjoyed doing Selfie Sprint! I think I will do it again next year!

.. image:: https://pbs.twimg.com/media/D56wr4nW4AcVeL6.jpg
    :width: 400

.. image:: https://pbs.twimg.com/media/D5600r5WkAEDxQh.jpg
    :width: 400


Seafood
-------

I went to see my brother for dinner. We had really great spicy seafood at Boiling Seafood Crawfish.

.. image:: https://instagram.fyvr4-1.fna.fbcdn.net/vp/21ef88439f3331f9aa4990f886749903/5D6E3634/t51.2885-15/sh0.08/e35/s750x750/57488426_1264143830402264_5360864775533430374_n.jpg?_nc_ht=instagram.fyvr4-1.fna.fbcdn.net
    :width: 400


Award
-----

I think the biggest highlight for me is receiving my `Community Service Award <http://pyfound.blogspot.com/2019/02/the-north-star-of-pycascades-core.html>`_ on Sunday.
Thank you Python community for this recognition! (`video <https://www.youtube.com/watch?v=P4IfFLAX9hY>`_)

.. image:: https://lh3.googleusercontent.com/kER4UTkQthe-c5t2LPaI2rvXB_TeD_WJNN6eCIHO6PApKV8FDkx-zwJeOOIxNu3WMNIO3pA4pKaIT06kgJDXqXbUe2LCX5q2aJJlSes2MubaizIlxkprG2djfHcLP0VaAf-LxKoSTUKp-wNzSGXHGsfXJxZghnN-z2la2HC3fLM2qAHCe8hT02gpd50AvRZsboMCmd2oLtbWsaIn0FC6aiSKue9vYVQzcmh__RNqJcPDKFmX2TLNSkx5x9BxU4dFZZtSr3lBZw0Hg7gmFgNl0lyuBcONGueS3QyzUcrsS-ERX17kCv_pgRCxLKyuabXQZ4_6paRtVp67yNQhmRfJPbhmGk1JAFnEJBTVB2-bQacpibiMKv6biEi1kilGmQQRHjMkoMIFMKqqWfikm2LTEjtr78m2SkycWdxsyzCgk6Pjkw96H6nnFUsDzeS1N0pJh2dSglySPI0RicAKn-8CA_8whMPowyN5EvsE0LvKnIxZ0SwsHaND7WLMFbBzn3v5bJfuFG7PvyDdxyTyoq97ANw622C0qsOkiW8z3I6J-E4z0NH_1X7iHM7B-ciQr6MltZV0haRmuebGV_AsZoDPL3-i_g_okf7lqR5QPHCf1iJgGfl1R9HLe6xMqdjXBVz3lX_zccIiFhE27hjsLSgkIu_R0N3izYz5LWaGtWdwAEPkEArubAeW0yWTCs9a6Z6kEJ6j2D_1UoJESoDV16CfstBp0g=w1000-h1333-no
    :width: 400


Until next time
---------------

I tried to include as many memories as I can into this post, but I'm unable to include
everything. 😥

PyCon 2019 has been inspiring. I learned a lot about the community, and I cried
a lot too (the good cry).

Thank you organizers, volunteers, sponsors, and all the wonderful Python community for these memories.
Let's do this again!

🌮
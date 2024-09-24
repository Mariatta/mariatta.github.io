---
title: "Python Core Sprint 2024: Day 1"
date: 2024-09-23T20:52:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "Python Core Sprint 2024: Day 1"
    identifier: python-core-sprint-2024-day-1
    weight: 20
tags: ["Python", "Open Source", "Sprint"]
images:
- /images/posts/pycoresprint2024selfie.jpg
hero: /images/posts/pycoresprint2024selfie.jpg
---

## Python Core Sprint 2024: Day 1

This week I'm in Bellevue for the annual Python core sprint. This year, the sprint is hosted at the Meta
Bellevue campus, and coordinated by Itamar Oren from Meta. Other Python core devs and contributors
who work at Meta are also helping (Dino Viehland,  Jason Fried, Matt Page, Parul Gupta, and Thomas Wouters).

The PSF offers travel grants for Python core devs who are participating in the sprint and aren't being
sponsored by their employer, which I signed up for. Thanks to the travel grant, my hotel stay is covered
fully by The PSF.

Thank you to Meta and The PSF for hosting and sponsoring! The sprint is one of my favorite Python events of the
year. At the sprint we all get to really focus and "work" on Python. It's also nice being able to talk face-to-face
IRL with other Python core team members. The sprint is only one of two events of the year in which there
are so many Python core team members all in the same room. (The other event being the Python language
summit at PyCon US.)

### DjangoCon US

I actually have online DjangoCon US registration (thanks to my consulting client!). When I woke up, the conference
just started, so I watched the morning keynote on my phone. The first keynote was by Sheena O'Connell, titled
"Power to the People who Teach the People". It was a great presentation, and I'd really recommend you to watch
it, especially if you're in a senior/lead dev role, or if you need to/want to mentor other devs.

Check out the slides [here](https://sheenarbw.github.io/pres-power-to-the-educators-djangoconus-2024/).

### (Got lost while) Getting to the venue

We were informed that there will be limited monitors available, and it's on a first-come-first-serve situation.
The night before, a group of core devs said they would meet at the hotel lobby at 9:15 before heading out together.
However, since I wanted to claim a monitor, I decided I'd go sooner than everybody else, at 8:30 AM. I 
asked if anyone else wanted to go together with me.
Turned out, almost everyone wanted to come at the same time.

Ok, so,... this large group of Python core devs went out together, we figured out the transit situation together,
and .... we all got lost together! 😂 When we arrived at the Meta building, we circled the entire block before
we finally found the entrance to the building lobby. This is what happened when you try to figure something out
before drinking your morning coffe 😓

### PyLadiesCon Program Committee

The PyLadiesCon program committee had a meeting. We discussed keynote selection, panels, and 
the program schedule.

### PyPodcats

Georgi reported that people weren't able to "search" for our podcast series, [PyPodcats](https://pypodcats.live),
on Spotify. She said that people needed to type in the "PyPodcats" in that exact capitalization on
Spotify to find the podcast. So I spent a bit of time investigating.

I still don't know how Spotify's algorithm work, but while investigating,
I found the [Podcast Specification Doc](https://providersupport.spotify.com/article/podcast-delivery-specification-1-9?_ga=2.171073635.258127355.1727124434-1695483710.1727124434)
from Spotify, which explains how the podcast RSS feed need to be structured and formatted for Spotify.

While reading the doc, I noticed that we did not have the `xmlns:spotify` attribute yet on our XML schema.
So I opened a PR to [add this attribute to our RSS feed](https://github.com/psf/the-invisibles/pull/44).

### Sprint Kick-off

At the kick-off, we went around the room and everyone introduced themselves, and stating what they'll be
working on during the sprint. Everyone has different things they wanted to work on:
freethreading, asyncio, dataclass, tag/template strings ([PEP 750](https://peps.python.org/pep-0750/)),
PEP process improvements, packaging (warehouse), etc.

### Python Contributing Guide 

Myself, I plan to focus on the work for Python Docs Editorial Board. One of the projects we're undertaking
is the re-working of the Python [DevGuide](https://devguide.python.org) into a "Contributing Guide". Ned Batchelder
has prepared an outline of what the new Contributing Guide could look like, and we're currently looking
for more feedback and eyes on it. If you have opinion about it, please check out the
[Discussion forum](https://discuss.python.org/t/refactoring-the-devguide-into-a-contribution-guide/63409) or
and [review the pull request](https://github.com/python/devguide/pull/1388).

### Unpopular Idea about Python Docs

I have something in mind about the state of Python Docs, but it's not gonna be popular among the Python core devs,
so I won't say out loud what it is yet 🤐 My idea is still just ... an idea. I don't even know if my idea
is even possible, so I still need to do some R&D on it.

I mentioned it to a few people, and they gave me some pointers on how to approach it. (Though none of them was
enthusiastic about it 😓)

Not sure how far can I get with this idea, but I'd like to at least try or to be one step closer towards a solution.
As part of this R&D effort, I'm currently reading the DevGuide from top to bottom, front and back.

While I was reading the Devguide, I noticed hidden inside the devguide, are two "TODO" items that seemed to have been there for almost
a year. So I opened some issues to hopefully address these TODOs. ([Issue 1408](https://github.com/python/devguide/issues/1408)
and [Issue 1409](https://github.com/python/devguide/issues/1409))

### Editorial Board Meeting Minutes

Since last month, the editorial-board has a [landing page](https://python.github.io/editorial-board/).

I added a small new feature to it: now there is a new
"[Board Members](https://python.github.io/editorial-board/members/)" page, and each board member
has their own landing page (and RSS Feed!) of the meetings in which they're an attendee.
([Here's my page](https://python.github.io/editorial-board/members/mariatta/)

I became interested to add this functionality after listening to Philip James' talk at PyBay about Automating
Your City Data with Python. In his talk, he demonstrated how to lookup city council minutes, what topic was discussed
during city council meetings, and which council members voted for which decisions.

I implemented this using what's called [taxonomies](https://gohugo.io/content-management/taxonomies/)
in Hugo. [PR with the change](https://github.com/python/editorial-board/pull/21).

I know this is an over-engineering of this simple meeting minutes, but I guess I just appreciate having
more structured data.

### Gidgethub

There was [a PR opened](https://github.com/gidgethub/gidgethub/pull/215) by Jacob Nesbitt on the
[Gidgethub](https://github.com/gidgethub/gidgethub) repository, for adding an ``expiration`` parameter to
``gidgethub.apps.get_jwt()``. This value is currently a hardcoded value of 10 minutes. The PR adds an optional parameter
that allows users to set a custom value, and defaults to 10 minutes, making it backward-compatible.
I thought it's a great improvement. I reviewed the PR and tested it locally.

### Python conference t-shirts

One weird thing you notice as a Python conference organizer, is which Python conference swag are being
used by your Python friends 😅

Today, I noticed a few people wearing different Python conference t-shirts, myself
included, so it was fun to see 😁

Python conference t-shirts worn by Python core devs today:
- PyCon Charlas 2024 (Guido)
- PyCon US 2024 (Lysandros)
- EuroPython 2023 (Hugo)
- PyCon US 2017 (Eric Snow)
- PyCon US 2016 (Thomas)
- PyCascades 2023 (Mariatta)

### Dinner

I went for Ramen and ice cream for dinner.

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/DASrQl8xDRa/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/DASrQl8xDRa/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/DASrQl8xDRa/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Mariatta Wijaya (@mariatta81)</a></p></div></blockquote>
<script async src="//www.instagram.com/embed.js"></script>


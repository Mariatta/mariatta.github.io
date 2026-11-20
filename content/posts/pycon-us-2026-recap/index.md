---
title: "PyCon US 2026 recap"
slug: "pycon-us-2026-recap"
date: 2026-11-19T08:00:00-08:00
description: "A recap of PyCon US 2026: volunteering, keynotes, my talk, the PyLadies lunch, sprints, and Pierogicon."
draft: false
menu:
  sidebar:
    name: PyCon US 2026 Recap
    identifier: pycon-us-2026-recap
    parent: posts
hero: /posts/pycon-us-2026-recap/pycon-us-2026-recap.jpg
tags:
  - PyCon
  - PyCon US
  - Python
  - Community
  - Open Source
---

The [PyCon US 2027 website](https://us.pycon.org/2027/) just launched, and the call for proposals is open. Yet my PyCon
US 2026 recap post has been sitting in draft for six months. So I thought I should finally finish it up now. Here goes.

{{<fosstodon user="mariatta" id="116573501213240070">}}

It was a great conference, and turned out to be a busy conference for me. Before heading to PyCon US, I actually felt
"free", like I didn't have many responsibilities other than running the Maintainer Summit and giving my talk. In the
end, I felt like every moment was filled with meeting and chatting with various people. I guess I tried to make the most
out of it by ensuring I get to actually speak face to face with people who I normally only interacted with online via
video calls and text messages.

## On helping, and being helped

When I arrived at the venue I ran into Elaine, who chaired the conference this year, and asked how things were going.
One of the things she brought up was that they needed more volunteers. Denny and Maria Jose, who run the Charlas track
and the En Español community booth, said the same: they needed more MCs for Charlas and more people to staff the booth.
As a conference organizer myself, I know that feeling well.

None of them asked me directly to volunteer. They were just sharing some frustrations about the issue. But then I signed
up to volunteer anyway. After everything they had already given to this conference, I wanted to give them something
back. So I ended up volunteering as an MC for the Charlas track, and I sat at the En Español community booth for an hour
to keep Maria Jose company.

{{<fosstodon user="mariatta" id="116579496946012679">}}

I don't speak Spanish, but I could still help. For the MC part, I wrote what I would say in English to introduce a
speaker, ran it through a translation tool, and asked Denny and Andres to check the translation. Then I practiced saying
it out loud in Spanish, and they checked that I pronounced it correctly. That was all it took.

While I was at the En Español booth with Maria Jose, a few attendees came up and started speaking Spanish to me. I
apologized.

{{<fosstodon user="mariatta" id="116581522106061325">}}

In both cases, Denny and Maria Jose could have said that only Spanish speakers can MC Charlas, or that only Spanish
speakers can staff the booth. They didn't. They let me help anyway.

So I was helping my friends. And in helping them, they were helping me: I got to practice and learn some Spanish.
Volunteering is mutual. It is supposed to be. I'm really glad I was able to help.

> **A small ask, while we're here:** if you saw someone volunteering at a conference, at a booth, in a session,
> anywhere: say thanks. Better, nominate them for an award. The work is mostly invisible, and the people doing it could
> use the visibility. More on this in my older post:
> [How to Say Thanks to Python People](/posts/how-to-thank-python-people/).

## Keynotes and talks

[Pablo Galindo Salgado's keynote](https://www.youtube.com/watch?v=e8uozuvRf7g) was in Spanish. We had the option to
listen to an auto-translated English version, but it sounded too robotic. I wanted to hear Pablo's real emotion in his
voice, so I read the English subtitles instead. He framed Python as a cathedral, the way Gaudí's Sagrada Família has
been under construction for 144 years and is only now nearing completion. What he built on top of that metaphor landed
hard: what AI is doing to open source contribution, how it is draining trust faster than the community can replenish it,
the eternal September we are walking into.

[amanda casari's keynote](https://www.youtube.com/watch?v=Z90Ax4SrhDQ) was the one I dragged myself to before going to a
clinic, not after, because I wasn't going to miss it. She talked about hope, autonomy, and agency. The difference
between automating and enabling. The difference between speed sold to us and pace we choose. _There are no solutions,
only trade-offs._ _Equal autonomy has never been granted or given, but it can be collectively won and defended._ I took
a lot of notes from that talk.

At the Maintainer Summit, Mike Fiedler gave a talk on PyPI safety, which was funny and bleak in equal measure:
legitimate-looking malicious packages now start at v1.0.4 instead of v0.0.1, because that's what an LLM told someone
"legitimate" looks like. And I chaired my friend Piper Thunstrom's
[CSS talk](https://www.youtube.com/watch?v=LIEsWtEUxrQ), which pointed us at stealthiswebsite.art and specifishity.com,
and told us to stop using `!important`.

## My own talk

📺 [Watch on YouTube](https://www.youtube.com/watch?v=bU_6lovnre0)

On Saturday I gave my talk:
[No More Spreadsheets! Building PyLadiesCon Infrastructure with Python and Django](https://us.pycon.org/2026/schedule/presentation/80/).

If you've been following along, you know this is my passion topic. It started as a lightning talk at last year's
Community Organizers Summit, grew into a full talk at [PyCascades in April](/posts/pycascades-2026-recap/), and this was
the refined version I promised back then. PyLadiesCon runs on a portal we built ourselves with Python and Django,
instead of a pile of spreadsheets, sign-up forms, and scheduling polls. The talk is the story of that portal: why we
built it, what it does for our volunteers and speakers, and why I think more communities should own their infrastructure
instead of renting it one spreadsheet at a time.

I'm happy with this talk.

{{<fosstodon user="mariatta" id="116588308950120363">}}

## The PyLadies lunch, and Laura

The main activity at the PyLadies lunch is sharing. Anyone can go up and talk about their story, their experience, or
something they accomplished in the past year. Honestly, to me, simply hearing about someone's journey is inspiring. It
really doesn't need to be about something super big.

At this lunch, we took the opportunity to share with the community the news about Laura Funderburk, who was an important
member of the PyLadies and Python community. We lost her in February. Georgi, Lais, Cheuk, Carol and I went up together
to remember her. I shared messages from her mother that had been read at her memorial. There isn't a clean way to write
about this. The room took a moment of silence in her honor. She was so motivated, and we truly miss her.

[![LinkedIn post from PyLadies Vancouver: We are deeply saddened to share the news of the passing of Laura Funderburk, a cherished and influential member of the Python and PyLadies Vancouver community. Laura was a brilliant speaker, a passionate developer advocate, and a leading figure in AI and data science, specializing in LLM applications, RAG systems, and agentic workflows. She shared her knowledge with our community, locally and globally, on stages like PyLadiesCon, PyLadies International Women's Day, Data Umbrella, and PyCon Charlas, always bringing clarity, curiosity, and care to complex topics. She authored a book, Building Natural Language and LLM Pipelines, helped practitioners build production-grade RAG systems, design thoughtful tool contracts, and approach context engineering with rigor. Through her writing and talks, she made advanced ideas accessible and practical for so many in our community. Laura's impact extends far beyond the events she spoke at or the pages she wrote. Laura will be profoundly missed in the Python community and beyond. Our thoughts are with her family, friends, and everyone whose life she enriched. For those who wish to pay their respects in person, a visitation and viewing is scheduled for Wednesday, March 4, 2026, from 3:00 to 4:00 pm at 219 6th Street, New Westminster, BC V3L 3A3. Laura will be profoundly missed in the Python community and beyond. Our thoughts are with her family, friends, and everyone whose life she enriched. Thank you, Laura, for everything you gave to this community.](images/pyladies-lunch/laura-linkedin-post.png)](https://www.linkedin.com/posts/pyladies-vancouver_laura-daniela-gutierrez-funderburk-obituary-activity-7435035650204184576-59w8)

## The sprints

At the sprints, the CPython team needed to print QR codes to clearly mark the sprint tables: codes pointing to Discord,
GitHub, and so on. Cam asked if I knew how to make them. Easy. I went to the QR code generator app I built myself,
generated the QR codes, and that was it. I felt like my purpose in life was complete.

{{<fosstodon user="mariatta" id="116596529377122719">}}

{{<fosstodon user="mariatta" id="116596672034550995">}}

Paul and I talked about the datetime docs, which was one of my follow-up items from the
[Python Docs Editorial Board meeting](https://python.github.io/editorial-board/updates/2026-04-14/#notes). Keith showed
me a framework he's been building for interactive docs and tutorials aimed at beginners who aren't programmers yet.
Daniel Chen and I talked about the PyLadiesCon portal, Django, and what's next for PyLadies Vancouver. Inessa and I did
a quick retro on the Maintainer Summit, which she and Leah and I ran together.

{{<fosstodon user="mariatta" id="116599737266844534">}}

## Friends winning things

I watched friends win things. Maria Jose and Denny got PyLadies Outstanding awards. Hwayoung Cha too. Jay got the PSF
Community Service Award. Congratulations to all of them! They truly deserve the recognition.

## Ice cream selfie flash mob

The ice cream selfie flash mob open space happened, and I was in awe. Maybe a hundred people showed up. I really didn't
expect so many. It took the whole hour for everyone to get their ice cream from Long Beach Creamery, who were
extraordinary about holding the line for us. It turned out to be their eleventh anniversary the same day. That felt like
the universe being a little kind. Thank you to everyone who showed up for the 41st ice cream selfie, ten years after the
first one.

{{<fosstodon user="mariatta" id="116590577506855911">}}

{{<fosstodon user="mariatta" id="116595796112900397">}}

## Pierogicon

Pierogicon started the first time PyCon US was in Cleveland. The first Pierogicon was just me, Anna Ossowski, and Jeff
Triplett going out to get pierogi together. The year after that, we brought more people to join us, and so it became a
tradition. However, not every PyCon US location has a pierogi culture, so we've had to improvise. Last year we did Thai
food instead. This year we went to a taco truck. The name stays; the cuisine rotates. Jeff even made an official
Pierogicon website: [pierogicon.com](https://pierogicon.com/). I love that we have a tradition where the whole point is
that the tradition is loose.

{{<fosstodon user="mariatta" id="116588421799835476">}}

## The quieter absences

There are also the people who weren't at PyCon at all this year. People who couldn't get a travel grant. People for whom
entry into the US has gotten harder. People who wouldn't come on principle. I think this part is worth acknowledging.

## What my body did

Those who saw me in person knew I wasn't feeling well. I started having a terrible migraine after my talk, and took the
rest of the day to rest. I went to an urgent care clinic and got some medication, but I still wasn't feeling 100%. I
pushed myself to take part in the rest of the conference anyway. I really shouldn't have.

When I got back home, I spent a few hours in the ER and finally got treated properly. I even got a brain scan, but the
result was nothing scary or concerning, so at least that was ruled out. Even then, it took another month of constantly
taking pain medication for me to feel normal again.

## Thanks

{{<fosstodon user="mariatta" id="116604061393820218">}}

A conference is a thousand things happening at once, and almost none of them happen without people doing the work no one
sees. Elaine chaired this one. She did it with the kind of leadership you only notice if you're paying attention: the
kind that makes everything look easy. Thanks to the PSF staff who worked entirely in the background; Olivia especially.
Thanks to the volunteers who showed up, and to Jon, who is taking over as chair next year: I am grateful, and a little
relieved on his behalf.

Thanks to everyone who came to my talk, and to everyone who came up to me afterward to say kind things, about the talk
and about the Python documentary. I do not always know what to do with kind words. I keep them anyway.

Thanks to the PyLadiesCon team, who are the best people I get to work with. Thanks to everyone who came to the
PyLadiesCon open space.

Thanks to Inessa and Leah, who I ran the Maintainer Summit with.

## Coming home

I'm grateful. I came home with too many small joys to count, a few quiet regrets, and a much better understanding of
where my own limits sit. I'll take it.

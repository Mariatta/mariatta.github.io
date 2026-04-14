---
title: "Travel Planning with AI"
date: 2026-04-14T07:00:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "Travel Planning with AI"
    identifier: travel-planning-with-ai
    weight: 20
tags: ["AI", "Travel", "PyCon", "Europe", "Learnings"]
images:
- /images/posts/travel-planning-with-ai.png
hero: /images/posts/travel-planning-with-ai.png
---

## Travel Planning with AI

I have started planning my family's travel with the assistance of Claude Code. It resulted in
a [website](https://mariatta.ca/portugal-trip/) that contains information about our travel destination,
potential activities we could take, hotel recommendations, restaurant suggestions, and even a checklist with
timelines for me to keep track of the planning progress, all the information needed in order to plan and decide
about our family vacation.

You can check the website [here](https://mariatta.ca/portugal-trip/). It was created 100% with Claude. I wrote no code.
I didn't even write the commit messages. I told Claude Code to do it on my behalf, even the creation of the
[GitHub Repo](https://github.com/mariatta/portugal-trip) and pushing it to my GitHub account, were all done by Claude.

In this post, I'm sharing my learning and thoughts about this experience so far.

## What Triggered All This

Our family is choosing where to go for our summer vacation this year. We are split between going to Europe
or Asia. Personally, I want to go to Europe somewhere, but my husband and kids are more interested in
visiting Asia (Taiwan, specifically).

Therefore, I needed a way to convince them to want to go to Europe. I needed to come up with a travel
plan and package that they can review and get excited about.

Usually I would spend days and weeks researching all the info about the travel destination on the internet. I would
then come up with a list, create a shareable doc and spreadsheet with timelines, activities, budget, and so on. 
There will be a lot of back and forth chats on Whatsapp with my husband.

Sometimes the travel would involve his family members, who are less experienced with collaborative docs and spreadsheets.
In that case, there would be a lot of copy pasting and re-sharing of the spreadsheets again and again.

But you know, this is 2026. Time to integrate some AI into everything.

## Why Portugal

Europe is big. At first, I didn't even know where to go in Europe. I thought of combining this with traveling
to a conference like [EuroPython](https://ep2026.europython.eu/). But the timing of EuroPython doesn't quite work out
this time.

Then, I found out that [PyCon Portugal](https://2026.pycon.pt/) will be happening on September 3-5,
coinciding with our wedding anniversary.
Therefore, I decided that it would be an even extra special to be able to celebrate our wedding anniversary, have
our family vacation, and to potentially speak at the conference at the same time. Therefore, I submitted a talk
proposal to PyCon Portugal hoping to get accepted. Whether it is a good idea or not to mix personal and professional
travel, is different discussion.

Anyway, I won't hear back from PyCon Portugal until maybe May or June (the [CFP](https://2026.pycon.pt/talks/cfp/)
is still open until April 30th). Even though personally I wanted to go anyway regardless of the CFP result,
my family members still need convincing, and so I still need to provide them with a travel plan.

## Why a Website

I wanted to create something visually appealing for my family to review, and I want to be able to share the results
of my research and planning. As mentioned, we used to share a Doc or Spreadsheets and a lot of copy pasting on Whatsapp.
This time I wanted to do something different. I thought of creating a PDF file. In fact, at first I prompted Claude and
ChatGPT to create a travel brochure for me in the form of PDF. However, somewhere along the way, I realized that I kept
asking it to add new information and to regenerate the PDF. 

Then I realized that regenerating PDF is not efficient. I realized that a website would be a more suitable way
for me to share information. I can keep updating the website content, and all I need is to share
the website URL with my family members. If they have any feedback or questions, I'm gonna update the website and
tell them to refresh it instead of sending them a new PDF.

After all, I'm a 9x serial conference organizer. I've been organizing and attending events for the last 10 years.
I know very well that every event needs a website. It is the most scalable way to share information than one-off PDFs.

## Which AI

I tried both ChatGPT and Claude to generate a travel plan for me. However, somewhere along the way when I
realized I wanted a website for it, I ended up continuing with just Claude, because I already have it set up and
integrated with my IDE for other coding-related tasks.

I have access to Claude Code Max as [a perk]({{< ref "posts/perks-of-python-core" >}}) of being a Python core developer.
Thanks to Gregory P. Smith for offering this perk to Python Core Developers!

## Working with AI

I tried several different prompts. When at first I told ChatGPT to create a website, it would just create a single html
file with the content and styles all at once.

While in general I don't really care which tool it uses, I still have my own opinion of how to best generate webpages,
and a single html file is not it.

So I decided to be more specific. I switched to Claude. Instead of telling Claude to create a website, this time
I started outlining additional requirements like, "host it on GitHub pages", and "use a static site generator".

I also asked it whether a static site generator would be suitable or should I use a backend
web framework. At that point, it recommends using just a static site generator and it chose Astro for me.
Of course I was dismayed that it did not choose Python, but to be honest, I agree that right now Astro is the better
choice when it comes to static site generators.

Claude then generated an entire Astro project, along with the Readme file and instructions for me on how to run it
locally, and how to deploy it to GitHub pages.

I then reviewed the generated website on the browser, and continued to iterate. As I reviewed the website,
I'd ask Claude to add new information, change up the dates, the color scheme, adding new pages and so on.

I really enjoy this process. It is much better to be able to review a personalized travel website and continuing
to update and add content to it.

Without the help of AI, I would have been reading the same info in the format of
boring URLs, search engine results, ad-ridden travel blogs from influencers, and copy-pasting all the time.
But now, this is a much more personalized experience. Not only that, I can still control the content and the layout
however I want. And I own the data. There is no cookie or tracking or whatever. I feel like I'm in control of things
and I feel comfortable sharing this website with my family members knowing that they are not going to be subjected to
ads or other tracking mechanisms.

You can review the full summary of my prompts in the [About](https://mariatta.ca/portugal-trip/about/) section of the website.

## Context Matters

In this project, my goal is not to write code. I also am not interested in learning how to build websites. I already
know how to do it. If I didn't already know how static-site generators work, I might not want to have it
all fully generated by AI. Or, I might not even know to tell it to use a static-site generator. I might have accepted
its first solution in the form of a single-page html file.

My goal here is just information-sharing. I don't actually care about the technical details. I didn't fully review
Claude's code. I didn't even review the commit messages. It's not like I'm contributing to an open source project
or doing this for paid work. This is truly personal project. Did it create superflous code? I don't know and don't care.

I would approach this differently if I expected someone else to use and review this. If this was a work project,
I would be more attentive about the code quality and the commit messages and so on. If this was an open source
project maintained by other people, I might not even use AI at all (depends on the project's policy around GenAI).

What about data accuracy? This is one of those things where accuracy is not a priority for me. At this point, whichever
travel websites I chose (and I have been planning travels for years, so I actually know it), they would all list pretty
much the same "Top 10 must do activities in Whatever City".

## Considering Personal Safety and Privacy

Isn't it dangerous to share all of these personal information about my travel plans, complete with dates, where I would
be, potential restaurants, and hotels where my family and I would be staying?

First of all, this is stil just a plan. I have not booked anything. Everything still depends on whether my talk gets
accepted, and whether our time off request gets approved.

Even if everything ends up happening, I'm ok with people knowing which dates I would be in Portugal. It would
probably become public knowledge eventually, especially if my talk is accepted and my name appears in the
conference schedule. And if my talk is not accepted, the dates might shift, and the final itinerary might look different.
We might not even go to Portugal.

Even though the AI-generated plan involves day-to-day itinerary, I know I won't end up sticking to it too much.

When it comes to hotel and food, I am very picky and opinionated. It is unlikely I will be staying at the
hotels listed. I asked AI to recommend hotels merely to provide an idea of the pricing and available choices.

I chose to share this website publicly, not only so that my family members can review and get excited about the trip,
but I also hope it could inspire others to plan their own travel this way (as opposed to using a third party
travel planning tool, or worse, spreadsheets or docs).

But what is interesting is that because I have source code of the website, I could choose to deploy it elsewhere else,
somewhere less public and less visible than GitHub pages.

## What's Next

Towards the end of my "conversation" with Claude, I started thinking that I might want to have a way to track my planning
progress, like keeping track of the timeline, reminding me to book hotels, and activities, and so on.

I was still unsure how to do this. If left to my own devices, I might create a Django backend for it. For now, Claude
believes it is not worth the effort considering this is just a website with the audience of four people. And I will
be the only user.

For now, I went along with just a plain checklist with local storage. I can check off the items as I go, and
it will be saved in my browser.

But what happens once my travel plan is finalized, and when I started booking my flights and hotels?
I kinda want to be able to display such information on the website so that my family members can see it.
But at the same time, I wouldn't want to share those information publicly.

I don't know yet how I would go about doing it. I have not tried asking Claude yet.
I'll wait until I hear about the talk decision from PyCon Portugal and go from there.

I also started thinking about other aspects of travel planning: the finances and budgeting. I usually have a spreadsheet
where I keep track of my travel expenses when abroad. It helps me plan for future travels by knowing how much I normally
spend in the past. I would like to share a high level information about our budget and expenses with my family as well
so that they too can be mindful and make informed decisions when planning for our activities together.
I have not yet decided whether I want to integrate this into the Claude-generated website or to keep it as a separate
spreadsheet.

At least I know I can always tell Claude to re-architect the whole thing based on my whims and ever-evolving needs and
requirements about my travel plan.

I wonder if other events could benefit from a website like this. Maybe company offsite events? Or other
smaller-scale social gatherings that are not conferences, but still require a lot of information sharing? The next
Python Core Sprint? Family reunions? What do you think? With GenAI, these things are easier to do now than ever before.

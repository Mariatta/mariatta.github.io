---
title: "The PyLadiesCon Portal Was Spammed: 2,249 Fake Accounts. Four Months Before Anyone Noticed"
slug: "pyladiescon-portal-spam-accounts"
date: 2026-09-17T07:21:00-07:00
description:
  "A post-mortem: a bot created 2,249 fake accounts on the PyLadiesCon portal to use it as a spam relay. Nobody noticed
  until four months later. What happened, why it worked, why it went undetected, and what changed."
draft: false
menu:
  sidebar:
    name: The PyLadiesCon Portal Was Spammed
    identifier: pyladiescon-portal-spam-accounts
    parent: posts
images:
  - /images/posts/pyladiescon-portal-spam-accounts.png
hero: /images/posts/pyladiescon-portal-spam-accounts.png
tags:
  - PyLadiesCon
  - Django
  - Open Source
  - Security
  - Maintainers
---

## PyLadiesCon Portal

[PyLadiesCon](https://conference.pyladies.com) is a free, online conference run entirely by volunteers. The
[PyLadiesCon portal](https://portal.pyladies.com) is where that work happens: it is where volunteers sign up and tell us
how they want to help, and where the organizing team keeps track of teams, tasks, and who has been reached. It replaced
the pile of Google Forms and spreadsheets we used to run the conference on, which is the story I told in my talk
[No More Spreadsheets](https://www.youtube.com/watch?v=bU_6lovnre0) at various conferences this year (PyCascades, LFNW,
PyCon US, and PyCon Portugal).

[Planning for PyLadiesCon 2026 is now underway](https://conference.pyladies.com/2026-special-edition/), and with it the
next round of portal work: speaker management, and more of the conference moving into the portal. It exists to serve one
conference a year for one community, and it is [open source](https://github.com/pyladies/pyladiescon-portal).

## What happened

Between May 16 and July 24 this year, a bot created **2,249 accounts** on the portal. For scale: in the thirteen months
before that, real humans had created 224. By the time I noticed, 91% of all accounts in the database were fake.

| Month                                  | Signups |
| -------------------------------------- | ------- |
| March 2025 to March 2026 (real people) | 224     |
| May 2026                               | 737     |
| June 2026                              | 894     |
| July 2026                              | 618     |
| August 2026                            | 1       |

Every one of the 2,249 looked the same. Username: ten random lowercase letters. First name: ten random lowercase
letters. Last name: same. The Code of Conduct box was ticked. The Terms of Service box was ticked. Yet the email never
got verified. Nobody ever logged in.

But the email addresses were not random. They were real. `firstname.lastname@` some real company, or an ordinary Gmail
or Yahoo address: 2,249 different ones across 842 domains.

## The portal was not the target. It was the weapon.

Two thousand accounts with real email addresses and gibberish names, none of them ever used. As someone who has watched
25 seasons of Law & Order, I had to ask the question that every detective asks: **what's the motive?**

The bot did not want accounts on the portal. **It wanted the portal to send email**. When you sign up, the portal emails
you a verification code. So if you feed a list of strangers' email addresses into the signup form, the portal will
dutifully send each stranger a "here is your verification code" message from a legitimate `pyladies.com` email address.

The accounts are just the litter. The email is the product.

Every one of those 2,249 messages was a real email, from a real domain with a clean sending history. That is what a
spammer cannot get on their own. Their own domains get burned within days; a freshly registered one is treated with
suspicion from the first message. A long-established community domain that sends a modest amount of legitimate mail is
worth far more, and they do not have to own it. They just need a form on it that will send to whatever address they type
in. We had one.

What the messages were for, was not immediately obvious to me. The verification email did not contain a link the spammer
controlled, so this was not phishing in the usual sense. The classic version of this attack puts a payload in a field
the email echoes back, so the username is "Claim your prize at some-link" and the portal mails it out under our name.
Ours were random letters, and Django's username validator would have stopped most of that anyway, so it was not that
either.

One of the things I considered was list validation, feeding a bought address list through our form to see which
addresses are alive, but that does not work here: bounces go to the sending domain's return path, which is ours, and the
spammer never sees them. Whatever the emails were for, the spammer benefited without ever seeing a single one.

That leaves the motive as **email bombing**. A target address gets signed up for hundreds of services at once, so that
real mail, say a password reset or a fraud alert from their bank, is buried under a pile of "verify your account"
messages and the target misses it. In that scheme the attacker does not need the email, only the fact that it was sent,
and the more legitimate the sender, the better it gets past filters. Ours was one small contribution to someone else's
flood. Whatever the exact scheme, the benefit to the spammer is the same: our reputation, our server, our postage, and
none of the consequences. And the consequences are real. Some of those 2,249 people will have hit "report spam", and
that mark lands on pyladies.com, the same domain the conference uses to reach its actual volunteers and sponsors.

None of this is new. Signup-form abuse is the kind of thing they teach in introductory web security: OWASP has had it in
[its catalogue of automated threats](https://owasp.org/projects/automated-threats-to-web-applications) for a decade, and
any form that sends mail to an address a visitor typed has been on the list of things to protect for as long as web
forms have sent mail. I knew these things happen. What I had not done was apply that knowledge to our own form, because
I just didn't expect that a volunteer portal for a small conference would be worth anyone's trouble. In hindsight, that
was the mistake: the question was never whether we were interesting, only whether the form would send. It would, and so
we should have guarded it from the start.

## How it happened

The portal is a Django app. The signup form had exactly one anti-abuse control: Django's CSRF token. Which is not an
anti-abuse control. It stops a _different_ website from submitting the form on your behalf; a bot that loads the page
first and reads the token is not forging anything.

There was a rate limit, sort of. django-allauth ships with a default of 20 signups per minute per IP address. Twenty per
minute per IP works out to 28,800 per day, per IP. The bot's busiest day was 111 signups total. It never got within
shouting distance of the limit, and I do not think that was an accident: the median gap between signups was 29 minutes,
spread evenly around the clock, for ten weeks. Slow and patient. A per-IP limit is built to catch a burst, and this was
the opposite of a burst.

The required checkboxes for the Code of Conduct and Terms of Service were, to a script, two more fields to set to `on`.
One hundred percent compliance.

And nothing ever got cleaned up. An account that never verifies its email just sits there, forever.

## Why there is a verification email in the first place

The irony is that the verification email, the thing that got abused, is there on purpose. It is one of the reasons we
have a web portal at all.

Before the portal existed, PyLadiesCon ran volunteer signups through Google Forms. It worked, mostly. But every year
some number of people typed their email address wrong, and we had no way to know until we tried to reach them and could
not. A volunteer who is excited enough to fill in the form and then never hears back from us, because `gmial.com` is not
a real domain, is a person we lost for no reason.

So when we built the portal, "the email address must be verified and reachable" was one of the first requirements. You
sign up, we send a code, you enter the code, and now we know we can reach you.

## How I found out

We didn't have any alerts or metrics set up, so we didn't find out until long after it had stopped.

We are starting to plan the next PyLadiesCon, and one of the first jobs is to look at what we have: how many volunteers
are coming back, how many accounts are dormant, what needs archiving. On September 10, I logged in to Django Admin on
the portal, checked the users list, and noticed that there were 2,475 user accounts.

I knew something was not right. I had just checked our [volunteer stats](https://portal.pyladies.com/stats/?year=2025),
and we do not have 2,475 volunteers. We do not have 2,475 of anything. And there was no reason for anyone to be signing
up at all: volunteer applications had closed months earlier, and the landing page no longer even mentioned them. But
closing the volunteer application form is not the same as closing account creation. The signup page is the standard
django-allauth route, and it stays up whether or not there is anything to sign up for. Nobody was supposed to be
arriving there, and 2,249 accounts had arrived anyway.

There is a particular sting in that for me. Last year I wrote a post on
[how to disable signup in django-allauth](https://mariatta.ca/posts/disabling-signup-django-allauth/), after strangers
created accounts on another app of mine after finding out about it from a conference talk. It is a few lines of code.
People still write to me to say it was exactly what they needed. I had the answer, I had published the answer, yet I did
not apply it to the one app of mine that other people actually depend on. Knowing how to close a door and remembering
that you left one open are, it turns out, different skills.

The Django Admin could not tell me _when_ the accounts had been created. The default list view had no creation date, and
no data export functionality. So before I could start on the analysis, I had to add those in first, and only then could
I see the problem clearly: when it started, the daily rate, the zero percent verified.

Here is the whole timeline. Times are Vancouver time (PDT, UTC−7).

| When                                        | What happened                                                                                                                                                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Friday, May 15, 8:10 PM (May 16, 03:10 UTC) | First spam signup                                                                                                                                                       |
| Friday, July 24                             | Last of the sustained run; a handful of stragglers followed in late July and August                                                                                     |
| Thursday, September 10                      | Noticed 2,475 accounts in the Django admin while auditing accounts ahead of PyLadiesCon 2026 planning                                                                   |
| Friday, September 11                        | Analysis written up in [#406](https://github.com/pyladies/pyladiescon-portal/issues/406); fix merged in [#407](https://github.com/pyladies/pyladiescon-portal/pull/407) |
| Tuesday, September 15                       | Fix deployed and running; the first scheduled cleanup removed the 2,249 accounts                                                                                        |

The gap between "found it" and "fixed it" was about a day. Getting the fix deployed and actually running took four more,
and two follow-up PRs that had nothing to do with the spam, which is its own small lesson about "landed" versus
"running", and why "did the scheduled jobs run" is first on the list of things the maintenance section grows to show.
The gap between "it started" and "found it" was **four months**.

## Why it wasn't found sooner

Because nothing was watching. The portal was built to serve one conference a year for a community that mostly finds it
through a link in a volunteer call. I check the admin when I have a reason to. For four months I had no reason to.

It also helps to be honest about the volume. Thirty signups a day is invisible if you are not counting. It is not a
spike, there was no outage, the site did not slow down, the mail did not bounce back to me. The attacker picked a rate
that would not trip anything, and it did not.

The portal does send the organizing team an email, but only when someone finishes a volunteer application, not when an
account is created. That is on purpose too. An account that has not verified its email address is not actionable, not
meaningful. I do not want a notification for every new user creation, and I still do not.

Which is why 2,249 of them went by without anyone on the team noticing: not one of them ever got as far as the thing we
normally care about.

There is a second reason that nothing was watching, and it is a choice I made deliberately: **the portal has no
analytics.** No Google Analytics, no Plausible, no tracking pixel. No third-party cookies unless we truly cannot do
without them. I care about the privacy of the people who use this thing, they are a very specific group of people
signing up for a very specific purpose, and I did not want to hand a list of them to anybody. I still think that was
right. But I will also say plainly that if we had had even basic analytics, a graph of signups per day would have looked
wrong in the first week, and somebody would have asked why.

We do have Sentry. It is one of the perks of being hosted on the PSF's infrastructure: we get access to the PSF's
Sentry, and it alerts me when the portal throws an exception. But that is what it watches for, errors, and there was no
error here. Every one of those 2,249 signups was the application doing exactly what it was written to do. A form was
submitted, a row was saved, an email went out, a 200 came back. Sentry had nothing to report because, from the code's
point of view, nothing went wrong.

So why not more alerts, the kind that enterprise products use, like New Relic, and Datadog, and their friends, with
thresholds on signups per hour and a page when they trip? Because those tools are built for production systems with a
team behind them, and the alerts only work if someone is on the other end of them. For a project of our scale they are a
burden: another account, another bill, another dashboard nobody is paid to look at, another stream of notifications for
a solo maintainer to learn to ignore. We do not have staff. We have me, and a handful of volunteers who already give
more than I have any right to ask.

What I do instead, and what I will keep doing, is check things by hand. This is not a new habit. During conference
planning and development, the months when the portal actually matters, we are in it constantly anyway: checking
sponsorship progress, counting volunteers, looking at who has signed up for what. The account sign up numbers now sit
alongside those, so looking at them costs nothing extra. When I am already there, the health of the portal is one more
thing I see.

The other side of that is the off-season. Between conferences the portal goes quiet, and so does the checking, and this
incident happened to land in exactly that gap. That is a real limitation, and I would rather say so than pretend a
paging setup I would never keep up with is the answer.

## Why there was no CAPTCHA

Sadly, I only have a very cliché response to this: as a volunteer-run web app, we have limited time and bandwidth to
implement the very best web app in the world.

We started developing the app in March 2025. We wanted it to be ready by PyCon US 2025 in May so we could begin
recruiting volunteers. So we had just the very bare minimum sign up form and email verification process. At the time,
the portal didn't even have PyLadiesCon branding on it. It was plain black and white web pages. We used almost all the
default settings that came with django and django allauth.

PyCon US happened. We made a big announcement, did a sprint. People started using it. Volunteers signed up, verified
their addresses, and applied. Nothing went wrong, and so we kept things as is. A year of clean signups looked like
evidence that the form was fine. The reason to add more "secure" guardrails never arrived.

I had also assumed that being obscure was a kind of protection: who is going to find a volunteer portal for a small
conference, and why would they bother? I wondered whether one of my talks had pointed someone at it. The timing looked
suspicious: the bot started on May 16, which is the day I gave the No More Spreadsheets talk at PyCon US. But the attack
started at 3 AM UTC that day, before I had spoken, and the video didn't even go up on YouTube until mid July. So it was
not the PyCon US talk. It could still have been an earlier one, or the link in the GitHub repo, which brings me to the
next section.

## Things I am still wondering about

**Did being open source make this easier?** I wonder. The entire portal is on GitHub, including the signup form, the
settings, and the fact that there was no CAPTCHA. Anyone who wanted to know exactly how the form behaved could read it
instead of probing it. I do not think that is what happened here, because the pattern is so generic: this is what you do
to _any_ form that emails a typed-in address, and you do not need the source to find one. But I cannot rule it out, and
I am not going to pretend the question does not nag at me. I am also not going to close the repo over it. The answer to
"the source shows there is no lock" is to add the lock, not to hide the door.

**Was it AI-driven?** It's possible. This is 2026. Hey, I've seen AI bots do worse to other open source maintainers. But
I have no proof that this was AI-driven. Email bombing is not a new technology. It is easy enough to write scripts and
automation to submit forms on websites. But I think that AI made it easier to scan and scrape open source GitHub
repositories to find web apps with vulnerabilities like this.

**I still want to know how they found the URL.** The portal is not linked from much. It shows up in my talks and in
emails to people who already know about PyLadiesCon. It is also the link on the project's GitHub repo. I'm curious which
one of these was the source for the attack.

## What could I have done to find out sooner?

I'm not sure.

An email on every signup? At thirty a day I would have muted it in a week, and then it would have been worse than
nothing, because I would have _believed_ I was watching. An additional chart in the dashboard would probably have done
it: a page in the portal that shows signups per day, verified against unverified. Two hundred signups and zero verified
is not subtle once it is in front of you. That is what I've built after this incident.

But I want to be careful not to pretend this was obvious in advance. This is a single-maintainer app with a narrow
purpose. It is not a product. There is no on-call rotation. The goal was to run our conference, and every hour spent
building monitoring for a threat I had not imagined was an hour not spent on the thing the app was for.

Could I have handled it pre-emptively? Sure, in the sense that a CAPTCHA takes an afternoon and I could have spent that
afternoon a year ago. But I would have had to know to. What I actually take from this is narrower and more useful: **any
form that sends an email to an address the visitor typed is a spam relay until proven otherwise.** I did not have that
rule before. I have it now, and going forward every personal Django app I build gets this guard from the start: a
CAPTCHA on any form that emails a visitor-typed address, a retention window on unverified accounts, and a number I
actually look at. Not because I expect to be targeted. Because I have learned that being targeted is not something you
have to do anything to deserve.

## What is the harm?

It is tempting to say "no real harm, they were just empty rows in the database, and storage is cheap."

That is not true, and it is worth spelling out exactly what it cost.

- The sending-reputation cost I described above: 2,249 unsolicited emails from pyladies.com, some fraction of them
  reported as spam. Of everything on this list, that is the one that outlasts the cleanup.
- The portal runs on infrastructure the PSF provides. Every fake signup was a database write, an outbound email and a
  slice of someone else's donated capacity. Small each time; ten weeks of it adds up.
- 2,249 people's email addresses sat in our database for four months. None of those people gave them to us; someone else
  typed them in. An email address is personal data, and holding personal data you were never given, for no purpose, is
  not a neutral act. Depending on where those people live, it is the kind of thing privacy law has opinions about, and I
  am not going to pretend a volunteer project is exempt just because it did not ask for the data. Those rows are gone
  now, and a scheduled task deletes any account that does not verify its email within the retention window, so the
  portal no longer keeps addresses it has no consent to keep.
- Four months of a database whose numbers could not be trusted. Any count we had looked at in that period would have
  been wrong.
- My time. Investigating, analyzing, fixing, deploying and confirming the fix took a week, and all of it pushed the
  speaker management work back by a week. The team needs that for PyLadiesCon 2026, and they needed it yesterday.
  Instead of building it, I spent the week cleaning up after a bot.

## What I did about it

All of the code for the things mentioned below landed in one pull request,
[pyladies/pyladiescon-portal#407](https://github.com/pyladies/pyladiescon-portal/pull/407), with the two deployment
follow-ups, [pyladies/pyladiescon-portal#408](https://github.com/pyladies/pyladiescon-portal/pull/408) and
[pyladies/pyladiescon-portal#409](https://github.com/pyladies/pyladiescon-portal/pull/409). It is now documented in the
[signup abuse protection](https://pyladiescon-portal-docs.netlify.app/architecture/signup-abuse-protection/)
architecture doc.

- **A CAPTCHA on signup.** This is the one that actually ends the pattern: it makes each signup cost more than one HTTP
  request, and the traffic goes somewhere cheaper. I went with
  [django-simple-captcha](https://pypi.org/project/django-simple-captcha/), which generates the image on our own server,
  rather than Cloudflare Turnstile or reCAPTCHA. A hosted CAPTCHA is stronger, no question, but it puts a third-party
  script on the page and hands the provider every visitor's IP address, and I was not going to fix a privacy-shaped
  problem by adding tracking. My rule for the portal has always been: reach for a third-party service only when we
  absolutely need one and there is no decent open-source, self-hosted library that does the job. Here there is one. If a
  future bot solves the images at volume, Turnstile is the fallback.
- **Real rate limits** as a backstop, in the shape that fits the app: a handful of signups per hour per IP, not twenty
  per minute.
- **Unverified accounts are deleted** by a scheduled task after a configurable number of days, and the verification
  email says so. If a stranger submits your address, the email you get tells you that you can ignore it and the account
  will be gone in a week.
- **The verification email no longer includes the username.** It used to say "user _whatever-you-typed_ has given your
  email address." That is attacker-controlled text going out under our domain. It now just says "someone".
- **An [architecture doc](https://pyladiescon-portal-docs.netlify.app/architecture/signup-abuse-protection/)**
  explaining why the CAPTCHA is there, so that in two years when it annoys someone, the answer to "do we really need
  this?" is written down.
- **A maintenance section** within the portal. For now, it shows metrics like signups per day, verified against
  unverified, and how many accounts are waiting to be deleted. It is behind its own permission, separate from the
  organizer role, because looking after the portal and running the conference are different jobs even when the same
  person does both. No email, no third-party monitoring service, just a number I actually look at.

That last one is the decision I expect to matter most in the long run. Every number the portal had ever shown was about
the conference: how many volunteers, how many sponsors, how far along the donation goal is. Those live on the organizer
dashboard and the public stats page, and they are the numbers we built the thing to track. There was no place for
numbers about the portal _itself_, and so the one metric nobody was showing, accounts created, is the one that went
sideways for four months without anyone noticing.

So the maintenance section is not really "the spam page". It is the start of a place for everything that is about the
health of the app rather than the progress of this year's event: whether the scheduled jobs ran and what they did,
whether the rate limits are being hit, whether email is bouncing, how fast the storage is growing. The rule for what
goes there is simple: would this number still matter if there were no conference this year? If yes, it is maintenance.
Each of those will be its own small page, added when there is a reason to, and read by whoever is looking after the
portal at the time, which for now is me.

The full analysis, with the numbers behind every claim in this post, is in
[pyladies/pyladiescon-portal#406](https://github.com/pyladies/pyladiescon-portal/issues/406); the changes are in
[#407](https://github.com/pyladies/pyladiescon-portal/pull/407).

## "This is why you just use Google Forms"

I can hear it, so let me answer it. Yes: this specific problem is one a third-party form would have solved for us.
Google would have absorbed the bot, and we would never have known it existed. Abuse protection is a real benefit of a
hosted form.

But that is one problem, and the reasons we built the portal in the first place, the ones I laid out in
[No More Spreadsheets](https://www.youtube.com/watch?v=bU_6lovnre0), are still there. Google Forms still does not solve
any of them: unreachable volunteers with typo'd addresses, data in a spreadsheet owned by whoever set the form up, no
way for a volunteer to see or update their own information, every organizer with edit access to everyone's personal
details, the community's data on a platform whose terms we do not set. A hosted form fixes the problem we did not have
last year and leaves every problem we did.

We left Google Forms because we wanted to own the process, and owning the process means owning the problems that come
with it. This was one of those problems. We got spammed once, and we fixed it in a week, on our own terms: a self-hosted
CAPTCHA because we do not want tracking, a maintenance page instead of a paging service, a retention window we set
ourselves. None of that is available on a form you rent. That is the trade, and knowing what I know now, I would take it
again.

If you maintain a small app with a signup form and you have never looked at how many accounts you have, go count them
now.

---

_If this post was useful and you want to support the work: PyLadiesCon 2026 is being planned right now, and it runs
entirely on volunteers and donations. You can [donate here](https://2026.conference.pyladies.com/en/donate/). If you are
at a company that sponsors community conferences,
[sponsorship details](https://2026.conference.pyladies.com/en/sponsors/) will be up soon._

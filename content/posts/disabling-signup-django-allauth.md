---
title: "Disabling Signup in Django allauth"
date: 2025-10-03T11:50:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "Disabling Signup in Django allauth"
    identifier: disabling-signup-django-allauth
    weight: 20
tags: ["Python", "Django", "Third Party Libraries", "Learnings"]
images:
- /images/posts/mariatta-djus2025-facepalm.JPG
hero: /images/posts/mariatta-djus2025-facepalm.JPG
---


## Django allauth

[Django allauth](https://allauth.org/) is a popular third party package that provides a lot of functionality for handling user authentication,
with support for social authentication, email verification, multi-factor authentication, and more.

It is a powerful library that greatly expands the built-in Django authentication system. It comes with its own basic
forms and models for user registration, login, logout, and password management.

I like using it because often I just wanted to get a new Django project up and running quickly without having to write
up all the authentication-related views, forms, and templates myself. I'm using `django-allauth` in [PyLadiesCon
Portal](https://portal.pyladies.com), and in my personal project [Secret Codes](https://secretcodes.dev).


## Why do I want to disable signup in a Django app?

I have my own personal QR Code generator which is a Django web app at [Secret Codes](https://secretcodes.dev).
If you want to know more of what it is all about, watch the recording of my talk from
[DjangoCon US 2025](https://2025.djangocon.us/talks/reverse-engineering-the-qr-code-generator-and-url-forwarder-service/)
(coming soon!), or check
my [slides](https://secretcodes.dev/mariatta-djangocon-slide).

For this app, I wanted to restrict the ability to generate dynamic URLS only for myself, while allowing
anyone to generate static QR codes without needing an account. Therefore, I hid that feature behind a login page.

I'm not prepared to handle a lot of traffic for the URL-redirection, and additionally, I don't want to be storing
other people's data like your name and email address. That's a lot of responsibility and there are legal requirements
that I'm need to follow. Maybe I'm supposed to be GDPR compliant and so on. I don't want to deal with all that for now.

This is just a hobby project. My goal for giving the talk was not to get people to sign up to my service, but rather
to give ideas and inspirations of what you could do with Django. I wanted to share a sample codebase so that you
don't have to start from scratch.

I'm actually really happy to hear that people got inspired from the talk and went to build their own version of a
QR code generator and URL shortener. That's what I really want out of this talk, to show that this is not difficult
to do on your own, and you don't have to settle for third party services.

Well, maybe once I figure out how to charge your credit card for this functionality, I might open up the sign up. 😊 

## Things I tried

I tried making the "Sign up" to be not so obvious. In the landing page of [Secret Codes](https://secretcodes.dev) site,
there is only a "Login" button, but
no "Sign up" button. I thought, sure people wouldn't try clicking the "Login" button before first finding
the "Sign Up" button.

Yet, after I presented my talk at DjangoCon US, I found out there are a few new accounts created on my app. 😳
Turns out they found the "Sign Up" page because the default `django-allauth` login page contains the "Sign up" link.

I didn't try the sign-up process myself. I didn't even set up the settings from django-allauth properly 😅
The login template page doesn't have fancy styles. I didn't even set up email verification process. I didn't
even know that the sign up would work. It's a magic of Django-allauth for having all of this works out of the box.
For myself, I created my own account using the `createsuperuser` management command. 🙃

At first, I considered just [updating the login template](https://docs.allauth.org/en/dev/common/templates.html)
and removing the "Sign up" link from the template.

But what if people could
still found the Sign up page directly by going to `/accounts/signup/` URL? After all, my code is open source, and if
people found out that I'm using `django-allauth`, they could guess what the sign up URL is by reading the
documentation.

Therefore it is not enough to simply hiding the "Sign up" link. It needs to be disallowed completely even when someone
found the URL.

## How to disable signup in Django allauth

This wasn't obvious in the official `django-allauth` documentation. I was searching for "disabling signup"
and didn't find anything there.

I found the solution by asking some AI chatbot, and I really wished it was written down in the documentation or in a tutorial
somewhere, so here goes.

1. Create an [AccountAdapter](https://docs.allauth.org/en/dev/account/adapter.html#allauth.account.adapter.DefaultAccountAdapter),
   returning `False` from `is_open_for_signup` method.

   For example, you could create a new file `adapters.py` in your Django app.


    ```python
    from allauth.account.adapter import DefaultAccountAdapter

    class NoSignupAccountAdapter(DefaultAccountAdapter):

       def is_open_for_signup(self, request):
           """
           Not open for signup.
           """
           return False
    ```

2. Set the `ACCOUNT_ADAPTER` setting to point to your custom adapter class.

   For example, if your `NoSignupAccountAdapter` class was defined in the `adapters.py` file in your Django app named
   `yoursite`, then you would add the following line to your Django `settings` file:

    ```python
    ACCOUNT_ADAPTER = "yoursite.adapters.NoSignupAccountAdapter"
    ```

And that's all.

With the above setting, when someone tries to access the sign up URL at `/accounts/signup`, they will see a message saying:

> We are sorry, but the sign up is currently closed."

At this time you could adjust the page template to make it look nicer or to say a different message by following the
instructions on how to [override the templates](https://docs.allauth.org/en/dev/common/templates.html#overriding-the-built-in-templates).

You can also see 
[the commit](https://github.com/Mariatta/secretcodes/commit/74629e026ab58473a9e9149d5b983076ab85defe)
I made in my repo for implementing this functionality.


Maybe you have your own reasons for disallowing sign ups in your Django app. Now you know how to do it.

## Thanks for reading 

Thanks for those who came to my talk at DjangoCon US, and for trying out my QR code generator at [Secret Codes](https://secretcodes.dev).
It's really encouraging to know that I'm not the only who needs a better way to generate QR codes. Really happy
to know that you find my project useful 😊

## About Django Allauth

- Repository: https://codeberg.org/allauth/django-allauth
- Documentation: https://docs.allauth.org/en/latest/
- On PyPI: https://pypi.org/project/django-allauth/
- License: MIT License

{{< alert type="info" >}}
Cover image is from my talk at DjangoCon US 2025, photo taken by [Colin Copeland](http://www.linkedin.com/in/colincopeland/).
{{< /alert >}}

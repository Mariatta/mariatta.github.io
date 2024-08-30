
---
title: "Extending the Django OAuth Toolkit Application Model Mid-project"
date: 2024-08-30T00:00:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "Extending the Django OAuth Toolkit Application Model Mid-Project"
    identifier: extending-dj-oauth-toolkit-model
    weight: 20
tags: ["Python", "Django", "Third Party Libraries", "Learnings", "Errors", "ORM", "Database"]
images:
- /images/posts/sep2020.jpg
hero: /images/posts/sep2020.jpg
---

## Django Oauth Toolkit

The [Django Oauth Toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/index.html) is a powerful library for
adding OAuth2 functionalities out of the box for your Django app.
The library comes with pre-defined models, views, urls, and templates for managing OAuth2 authorization and flow.

## The Application Model

Django OAuth Toolkit provides a basic model for the OAuth2 Application, this is a model that represents a Client on
the Authorization server. It has fields like ``client_id``, ``user``, ``redirect_uris``, ``client_secret``, etc.

## Extending the Application Model

Perhaps you may need to extend the ``Application`` model with your own's custom fields. For example, as described in the Django
OAuth Toolkit documentation, you might want to add a logo to your Application, or adding a flag to agreeing to the
terms of use, etc.

It can be done by extending the ``oauth2_provider.models.AbstractApplication``.

The key thing though, you must do this at the **very beginning** of your project, **before** you ran the initial ``oauth2_provider``
migration step.

The documentation explains [how to do this](https://django-oauth-toolkit.readthedocs.io/en/latest/advanced_topics.html#AbstractApplication).

1. Create a new Custom Application:

    ```python
    from django.db import models
    from oauth2_provider.models import AbstractApplication

    class MyApplication(AbstractApplication):
        logo = models.ImageField()
        agree = models.BooleanField()
    ```

2. Update the Django settings, add the ``OAUTH2_PROVIDER_APPLICATION_MODEL`` variable, pointing to the new custom app:

    ```python
    OAUTH2_PROVIDER_APPLICATION_MODEL = "your_app_name.MyApplication"
    ```

3. Creating new model means that you need to create the migration for it, by running:

    ```bash
    python manage.py makemigrations your_app_name
    ```

4. Force the migration of your new model, ensuring it to be run before the ``oauth2_provider`` migrations.
   Add to your app's migration file:

    ```python
    run_before = [
        ("oauth2_provider", "0001_initial"),
    ]
    ```

5. Run the django migration.
    ```bash
    python manage.py migrate
    ```

## Extending the Application Model mid-project

As mentioned above, the documented way to use a custom ``Application`` model is by creating it at
the beginning of the project.

But, maybe you're using this library for the first time. You didn't know you'd need a custom model.
You ended up just using the built-in model, deployed to production. Maybe much later in the development cycle, you then realized that you
need to extend it.

What if you need to create the new custom application model after the initial migration ``oauth2_provider`` has been run? 

This is what happened in my client's project. We had a project going that's been using the built-in ``Application`` model,
however now the project requirement changed, and we needed to extend it.

When I tried swapping the ``Application`` model with a custom one, I got some errors when running the migration, or when using the token.

Here are some example error messages that we've seen:

```
Migration oauth2_provider.0001_initial is applied before its dependency
    your_app_name.0001_initial on database 'default'.
```

```
insert or update on table "oauth2_provider_accesstoken" violates foreign key constraint
    "oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr"
    DETAIL:  Key (application_id)=(3) is not present in table "oauth2_provider_application".
```

## What to do about it

When I first saw the message about a migration being applied before the dependency app, I thought, perhaps I could
just reset the migration, like:

```bash
python manage.py migrate oauth2_provider zero
```

However, it didn't work, because the migration is not reversible.

After some trial and error, I found some workaround. 

{{< alert type="danger" >}} 
Before you go ahead and copy-paste the snippets below, please read the aftermath first to understand the risks.
{{</alert>}}

Here's what happened in the end.

- Downtime.
- Deployment stopped.
- Co-workers complained about broken local environment.
- Tables got dropped.
- Existing OAuth apps got deleted.
- Existing users needed to re-create their OAuth Applications. (And update their client id/secret, etc.)

Not good. In my client's case, the users of the OAuth Applications are quite small, and rather internal, so the downtime
was something we could bear. This might not work for you, and perhaps, I mean, **surely** there's a better way to do it?

Anyway, here are the things I did, just in case you have the same problem we faced, and you want to proceed anyway.

1. Make the code changes as mentioned above, ie. create the custom ``Application`` model, update the ``settings``
   file, set the ``OAUTH2_PROVIDER_APPLICATION_MODEL`` setting, create the migration file, and add the ``run_before`` step
   to it. But, do not run the migration file. (Well you can run it, but you'll get an error, so it just won't work).


2. Go back to the model's migration file, and comment the code where it says ``run_before``.

   ```
   # run_before = [
   #    ("oauth2_provider", "0001_initial"),
   # ]
   ```

3. Go back to the settings, and comment out the line for ``OAUTH2_PROVIDER_APPLICATION_MODEL``.

   ```
   # OAUTH2_PROVIDER_APPLICATION_MODEL = "your_app_name.MyApplication"
   ```

4. Revert the ``oauth2_provider`` migration using ``--fake``:

   ```bash
   python manage.py migrate --fake oauth2_provider zero
   ```

5. Restore the changes from step 2. and 3. above. Eg uncomment the ``run_before``, and the ``OAUTH2_PROVIDER_APPLICATION_MODEL`` lines.

   Eg. make sure the code looks like this again:

    ```python
   OAUTH2_PROVIDER_APPLICATION_MODEL = "your_app_name.MyApplication"
   ```
   
   and

    ```python
    run_before = [
        ("oauth2_provider", "0001_initial"),
    ]
   ```

6. On the terminal, open Django dbshell.

   ```bash
   python manage.py dbshell
   ```

7. Inside the ``dbshell``, drop the ``oauth2_provider`` tables.

   ```sql
   DROP TABLE oauth2_provider_accesstoken CASCADE;
   DROP TABLE oauth2_provider_grant CASCADE;
   DROP TABLE oauth2_provider_idtoken CASCADE;
   DROP TABLE oauth2_provider_refreshtoken CASCADE;
   ```
   
8. Exit ``dbshell``.

   ```
   \q
   ```

9. Now the Django migration can run without errors.

   ```bash
   python manage.py migrate
   ```

I did all the steps from 1 to 9 above, it worked for me locally. But now the trouble is, how to deploy such a change?

Here's what we end up doing. (which caused the deployment to stop, and co-workers "complained").

I committed the code changes mentioned on step 1 (and then pushed, and merged the PR). This way my co-workers
(and the staging environment) received the code containing the new model and migration files.

Then I told them that they need to do steps 2-9 on their own. eg. ask them to comment
a few lines of code, drop their tables, and uncomment the codes again, and re-run their migration. I've
included the documentation and step-by-step instructions just like the one I wrote above, and additionally offered
to pair program and help them resolve it.

We did this change on the staging environment too.
After making sure that the process worked like this on staging, (and after confirming that co-workers' issues are resolved)
that's when we deployed to production and break the production for a few minutes.

## Is there a better way to do this?

I'm sure the way I did it is not the right way to fix it. Not everyone can afford such downtime.

If you know of a better way, please let me know, or update [the issue](https://github.com/jazzband/django-oauth-toolkit/issues/669).

I'm wondering, perhaps the useful thing to do is to just always begin with a custom Application model from the get go. Right now,
the topic about extending the Application model is not mentioned in the "Get Started" documentation, but appears much later
under "Advanced topics."

Perhaps the docs should recommend user to always create the custom Application, even if they don't need additional fields.

Perhaps it should be written in bold somewhere that "using the built-in Application model means you can't change it down the road".

Anyway, thanks for reading, and I hope you find it useful.

## About Django OAuth Toolkit

- GitHub Repo: https://github.com/jazzband/django-oauth-toolkit
- Documentation: https://django-oauth-toolkit.readthedocs.io/en/latest/
- On PyPI: https://pypi.org/project/django-oauth-toolkit/
- License: BSD License
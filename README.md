# Django Boilerplate

[![Build Status](https://img.shields.io/github/actions/workflow/status/devxhub/django-boilerplate/ci.yml?branch=main)](https://github.com/devxhub/django-boilerplate/actions/workflows/ci.yml?query=branch%3Amain)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest)](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/devxhub/django-boilerplate/main.svg)](https://results.pre-commit.ci/latest/github/devxhub/django-boilerplate/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Features

- For Django 4.1
- Works with Python 3.11
- Renders Django projects with 100% starting test coverage
- Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
- [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Registration via [django-allauth](https://github.com/pennersr/django-allauth)
- Social Authentication by Google, Facebook
- DRF and Graphql API 
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Optional custom static build using Gulp or Webpack
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default or Amazon SES if AWS is selected cloud provider, but switchable)
- OTP Verification 
- Media storage using Amazon S3, Google Cloud Storage, Azure Storage or nginx
- Docker support using [docker-compose](https://github.com/docker/compose) for development and production (using [Traefik](https://traefik.io/) with [LetsEncrypt](https://letsencrypt.org/) support)
- [Procfile](https://devcenter.heroku.com/articles/procfile) for deploying to Heroku
- Instructions for deploying to [PythonAnywhere](https://www.pythonanywhere.com/)
- Run tests with unittest or pytest
- Customizable PostgreSQL and MySQL version
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Optional Integrations

_These features can be enabled during the initial project setup._

- Serve static files from Amazon S3, Google Cloud Storage, Azure Storage or [Whitenoise](https://whitenoise.readthedocs.io/)
- Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
- Integration with [MailHog](https://github.com/mailhog/MailHog) for local email testing
- Integration with [Sentry](https://sentry.io/welcome/) for error logging
- Integration with [Twilio](https://www.twilio.com/) for SMS services
- Integration with [Selenium](https://www.selenium.dev/) for browser testing
- PGAdmin4 for PostgreSQL database management (Docker setup only)

## Constraints

- Only maintained 3rd party libraries are used.
- Uses PostgreSQL everywhere: 10.19 - 14.1 and MySQL 5.7, 8.0, and 8.0.29  are also available.
- Environment variables for configuration (This won't work with Apache/mod_wsgi).

## Usage

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then edit the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter. Trust me, it's awesome:
```sh
pip install "cookiecutter>=1.7.0"
```
Now run it against this repo:
```sh
cookiecutter https://github.com/devxhub/django-boilerplate
```
You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your information.

Answer the prompts with your own desired [options](http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html). For example:

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [My Awesome Project]: Reddit Clone
    project_slug [reddit_clone]: reddit
    description [Behold My Awesome Project!]: A reddit clone.
    author_name [DEVxHUB AIS Team]: Devxhub AIS
    domain_name [example.com]: myreddit.com
    email [devxhub-ais@example.com]: devxhub@gmail.com
    version [0.1.0]: 0.0.1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select username_type:
    1 - email
    2 - username
    Choose from 1, 2 [1]: 1
    timezone [UTC]: America/Los_Angeles
    windows [n]: n
    Select an editor to use. The choices are:
    1 - none
    2 - pycharm
    3 - vscode
    Choose from 1, 2, 3 [1]: 1
    use_docker [n]: y
    Select database_engine:
    1 - postgresql
    2 - mysql
    Choose from 1, 2 [1]: 2
    Select database_version:
    1 - postgresql@14
    2 - postgresql@13
    3 - postgresql@12
    4 - postgresql@11
    5 - postgresql@10
    6 - mysql@8.0.30
    7 - mysql@8.0
    8 - mysql@5.7
    Choose from 1, 2, 3, 4, 5, 6, 7, 8 [1]: 1
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]: 1
    Select mail_service:
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - SendinBlue
    8 - SparkPost
    9 - Other SMTP
    Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]: 1
    use_async [n]: n
    use_selenium [n]:y
    use_drf [n]: n
    use_graphene[y]: y
    use_twillio[n]:y
    Select frontend_pipeline:
    1 - None
    2 - Django Compressor
    3 - Gulp
    4 - Webpack
    Choose from 1, 2, 3, 4 [1]: 1
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry [n]: y
    use_whitenoise [n]: n
    use_heroku [n]: y
    Select ci_tool:
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    Choose from 1, 2, 3, 4 [1]: 4
    keep_local_envs_in_vcs [y]: y
    debug [n]: n

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

- [Developing locally](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)
- [Developing locally using docker](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)


## For Readers of Two Scoops of Django

You may notice that some elements of this project do not exactly match what we describe in Chapter 3. The reason for that is this project, amongst other things, serves as a test bed for trying out new ideas and concepts. Sometimes they work, sometimes they don't, but the end result is that it won't necessarily match precisely what is described in the book I co-authored.

## "Your Stuff"

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.



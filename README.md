# Django Boilerplate

[![Build Status](https://img.shields.io/github/actions/workflow/status/devxhub/django-boilerplate/ci.yml?branch=main)](https://github.com/devxhub/django-boilerplate/actions/workflows/ci.yml?query=branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/devxhub/django-boilerplate/main.svg)](https://results.pre-commit.ci/latest/github/devxhub/django-boilerplate/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Features

- For Django 4.1
- Works with Python 3.12
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
and then edit the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [dxh-py](https://github.com/devxhub/dxh-py) to do all the work.

First, get `dxh-py`. Trust me, it's awesome:

```sh
pip install dxh-py
```
Now run it against this repo:

```sh
dxh_py https://github.com/devxhub/django-boilerplate
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'DEVxHUB', 'devxhub@example.com', etc to your information.

Answer the prompts with your own desired. For example:

```sh
    You've downloaded /home/django-boilerplate before. Is it okay to delete and re-download it? [y/n] (y): y
  [1/30] project_name (My Awesome Project): Your Project Name
  [2/30] project_slug (my_awesome_project): your_project_name
  [3/30] description (Behold My Awesome Project!): 
  [4/30] author_name (DEVxHUB): 
  [5/30] domain_name (example.com): 
  [6/30] email (devxhub@example.com): 
  [7/30] version (0.1.0): 
  [8/30] Select open_source_license
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from [1/2/3/4/5] (1): 
  [9/30] Select username_type
    1 - email
    2 - username
    Choose from [1/2] (1): 
  [10/30] timezone (UTC): 
  [11/30] windows (n): 
  [12/30] Select editor
    1 - none
    2 - vscode
    3 - pycharm
    Choose from [1/2/3] (1): 
  [13/30] use_docker (n): 
  [14/30] Select database_engine
    1 - postgresql
    2 - mysql
    Choose from [1/2] (1): 
  [15/30] Select database_version
    1 - postgresql@16
    2 - postgresql@15
    3 - postgresql@14
    4 - postgresql@13
    5 - postgresql@12
    6 - mysql@8.0.30
    7 - mysql@8.0
    8 - mysql@5.7
    Choose from [1/2/3/4/5/6/7/8/9/10] (1): 
  [16/30] use_tenants (n): 
  [17/30] Select cloud_provider
    1 - AWS
    2 - GCP
    3 - Azure
    4 - None
    Choose from [1/2/3/4] (1): 
  [18/30] Select mail_service
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - Brevo
    8 - SparkPost
    9 - Other SMTP
    Choose from [1/2/3/4/5/6/7/8/9] (1): 
  [19/30] use_async (n): 
  [20/30] use_drf (n): 
  [21/30] use_graphene (n): 
  [22/30] Select frontend_pipeline
    1 - None
    2 - Django Compressor
    3 - Gulp
    4 - Webpack
    Choose from [1/2/3/4] (1): 
  [23/30] use_celery (n): 
  [24/30] use_mailhog (n): 
  [25/30] use_sentry (n): 
  [26/30] use_whitenoise (n): 
  [27/30] use_heroku (n): 
  [28/30] Select ci_tool
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    Choose from [1/2/3/4] (1): 
  [29/30] keep_local_envs_in_vcs (y): 
  [30/30] debug (n): 
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

## Creating Your First Django App

After setting up your environment, you’re ready to add your first app. This project uses the setup from “Two Scoops of Django” with a two-tier layout:

- Top Level Repository Root has config files, documentation, manage.py, and more.

- Second Level Django Project Root is where your Django apps live.

- Second Level Configuration Root holds settings and URL configurations.

The project layout looks something like this:

    <repository_root>/
    ├── config/
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── local.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── <django_project_root>/
    │   ├── <name_of_the_app>/
    │   │   ├── migrations/
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   ├── __init__.py
    │   └── ...
    ├── requirements/
    │   ├── base.txt
    │   ├── local.txt
    │   └── production.txt
    ├── manage.py
    ├── README.md
    └── ...

Following this structured approach, here’s how to add a new app:

1. Create the app using Django’s `startapp` command, replacing `<name-of-the-app>` with your desired app name:

```sh
python manage.py startapp <name-of-the-app>
```

2. Move the app to the Django Project Root, maintaining the project’s two-tier structure:

```sh 
mv <name-of-the-app> <django_project_root>/
```
3. Edit the app’s `apps.py` change name = `'<name-of-the-app>'` to name = `'<django_project_root>.<name-of-the-app>'`.

4. Register the new app by adding it to the `LOCAL_APPS` list in `config/settings/base.py`, integrating it as an official component of your project.

## "Your Stuff"

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.



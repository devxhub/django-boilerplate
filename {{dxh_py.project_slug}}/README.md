# {{dxh_py.project_name}}

{{ dxh_py.description }}

[![Built with Django-Boilerplate](https://img.shields.io/badge/Built%20with-Django%20Boilerplate-ff69b4.svg?logo=Django-Boilerplate)](https://github.com/devxhub/django-boilerplate/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

{%- if dxh_py.open_source_license != "Not open source" %}

License: {{dxh_py.open_source_license}}
{%- endif %}

## Settings

Moved to [settings](http://dxh_py-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy {{dxh_py.project_slug}}

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://dxh_py-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

{%- if dxh_py.use_celery == "y" %}

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd {{dxh_py.project_slug}}
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd {{dxh_py.project_slug}}
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd {{dxh_py.project_slug}}
celery -A config.celery_app worker -B -l info
```

{%- endif %}
{%- if dxh_py.use_mailhog == "y" %}

### Email Server

{%- if dxh_py.use_docker == "y" %}

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [dxh_py-django Docker documentation](http://dxh_py-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`
{%- else %}

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [MailHog](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface will be available.

1.  [Download the latest MailHog release](https://github.com/mailhog/MailHog/releases) for your OS.

2.  Rename the build to `MailHog`.

3.  Copy the file to the project root.

4.  Make it executable:

        $ chmod +x MailHog

5.  Spin up another terminal window and start it there:

        ./MailHog

6.  Check out <http://127.0.0.1:8025/> to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

{%- endif %}

{%- endif %}
{%- if dxh_py.use_sentry == "y" %}

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=dxh_py> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
{%- endif %}

## Deployment

The following details how to deploy this application.
{%- if dxh_py.use_heroku.lower() == "y" %}

### Heroku

See detailed [dxh_py-django Heroku documentation](http://dxh_py-django.readthedocs.io/en/latest/deployment-on-heroku.html).

{%- endif %}
{%- if dxh_py.use_docker.lower() == "y" %}

### Docker

See detailed [dxh_py-django Docker documentation](http://dxh_py-django.readthedocs.io/en/latest/deployment-with-docker.html).

{%- endif %}
{%- if dxh_py.frontend_pipeline in ['Gulp', 'Webpack'] %}

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
{%- endif %}

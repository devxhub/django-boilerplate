.. _template-options:

Project Generation Options
==========================

This page describes all the template options that will be prompted by the `django-boilerplate CLI`_ prior to generating your project.

.. _django-boilerplate CLI: https://github.com/devxhub/django-boilerplate

project_name:
    Your project's human-readable name, capitals and spaces allowed.

project_slug:
    Your project's slug without dashes or spaces. Used to name your repo
    and in other places where a Python-importable version of your project name
    is needed.

description:
    Describes your project and gets used in places like ``README.rst`` and such.

author_name:
    This is you! The value goes into places like ``LICENSE`` and such.

email:
    The email address you want to identify yourself in the project.

username_type:
    The type of username you want to use in the project. This can be either
    ``username`` or ``email``. If you choose ``username``, the ``email`` field
    will be included. If you choose ``email``, the ``username`` field will be
    excluded. It is best practice to always include an email field, so there is
    no option for having just the ``username`` field.

domain_name:
    The domain name you plan to use for your project once it goes live.
    Note that it can be safely changed later on whenever you need to.

version:
    The version of the project at its inception.

open_source_license:
    A software license for the project. The choices are:

    1. MIT_
    2. BSD_
    3. GPLv3_
    4. `Apache Software License 2.0`_
    5. Not open source

timezone:
    The value to be used for the ``TIME_ZONE`` setting of the project.

windows:
    Indicates whether the project should be configured for development on Windows.

editor:
    Select an editor to use. The choices are:

    1. none
    2. pytharm_
    3. vscode_


use_docker:
    Indicates whether the project should be configured to use Docker_, `Docker Compose`_ and `devcontainer`_.

database_version:
    Select the version of the database you want to use for your project.

    .. note::
        | Database versions are shown in the format ``{database_engine}@{version}``.
        | So make sure you select the versoin accoring to the database version you seleted in the previous step.
        | For example, if you selected **Postgres** as your database, make sure to select from one of the options starting with ``postgresql@{version_you_want}`` and if you seleted **MySQL**, select one of the options starting with ``mysql@{version_you_want}``.

    *Currently, following PostgreSQL versions are supported:*

    1. 16
    2. 15
    3. 14
    4. 13
    5. 12

    *Currently, following MySQL versions are supported:*

    1. 8.0
cloud_provider:
    Select a cloud provider for static & media files. The choices are:

    1. AWS_
    2. GCP_
    3. Azure_
    4. None

    If you choose no cloud provider and docker, the production stack will serve the media files via an nginx Docker service. Without Docker, the media files won't work.

mail_service:
    Select an email service that Django-Anymail provides

    1. Mailgun_
    2. `Amazon SES`_
    3. Mailjet_
    4. Mandrill_
    5. Postmark_
    6. SendGrid_
    7. `Brevo (formerly SendinBlue)`_
    8. SparkPost_
    9. `Other SMTP`_

use_async:
    Indicates whether the project should use web sockets with Uvicorn + Gunicorn.

use_drf:
    Indicates whether the project should be configured to use `Django Rest Framework`_.

use_graphene:
    Indicates whether the project should be configured to use Graphene_. 

frontend_pipeline:
    Select a pipeline to compile and optimise frontend assets (JS, CSS, ...):

    1. None
    2. `Django Compressor`_
    3. `Gulp`_
    4. `Webpack`_

Both Gulp and Webpack support Bootstrap recompilation with real-time variables alteration.

use_celery:
    Indicates whether the project should be configured to use Celery_.

use_mailhog:
    Indicates whether the project should be configured to use MailHog_.

use_sentry:
    Indicates whether the project should be configured to use Sentry_.

use_whitenoise:
    Indicates whether the project should be configured to use WhiteNoise_.

use_heroku:
    Indicates whether the project should be configured so as to be deployable
    to Heroku_.

ci_tool:
    Select a CI tool for running tests. The choices are:

    1. None
    2. `Travis CI`_
    3. `Gitlab CI`_
    4. `Github Actions`_
    5. `Drone CI`_

keep_local_envs_in_vcs:
    Indicates whether the project's ``.envs/.local/`` should be kept in VCS
    (comes in handy when working in teams where local environment reproducibility
    is strongly encouraged).
    Note: .env(s) are only utilized when Docker Compose and/or Heroku support is enabled.

debug:
    Indicates whether the project should be configured for debugging.
    This option is relevant for Django Boilarplate developers only.


.. _MIT: https://opensource.org/licenses/MIT
.. _BSD: https://opensource.org/licenses/BSD-3-Clause
.. _GPLv3: https://www.gnu.org/licenses/gpl.html
.. _Apache Software License 2.0: http://www.apache.org/licenses/LICENSE-2.0

.. _pycharm: https://www.jetbrains.com/pycharm/
.. _vscode: https://github.com/microsoft/vscode

.. _Docker: https://github.com/docker/docker
.. _Docker Compose: https://docs.docker.com/compose/
.. _devcontainer: https://containers.dev/

.. _PostgreSQL: https://www.postgresql.org/docs/

.. _Gulp: https://github.com/gulpjs/gulp
.. _Webpack: https://webpack.js.org

.. _AWS: https://aws.amazon.com/s3/
.. _GCP: https://cloud.google.com/storage/
.. _Azure: https://azure.microsoft.com/en-us/products/storage/blobs/

.. _Amazon SES: https://aws.amazon.com/ses/
.. _Mailgun: https://www.mailgun.com
.. _Mailjet: https://www.mailjet.com
.. _Mandrill: http://mandrill.com
.. _Postmark: https://postmarkapp.com
.. _SendGrid: https://sendgrid.com
.. _Brevo (formerly SendinBlue): https://www.brevo.com
.. _SparkPost: https://www.sparkpost.com
.. _Other SMTP: https://anymail.readthedocs.io/en/stable/

.. _Django Rest Framework: https://github.com/encode/django-rest-framework/

.. _Graphene: https://github.com/graphql-python/graphene

.. _Django Compressor: https://github.com/django-compressor/django-compressor

.. _Celery: https://github.com/celery/celery

.. _MailHog: https://github.com/mailhog/MailHog

.. _Sentry: https://github.com/getsentry/sentry

.. _WhiteNoise: https://github.com/evansd/whitenoise

.. _Heroku: https://github.com/heroku/heroku-buildpack-python

.. _Travis CI: https://travis-ci.org/

.. _GitLab CI: https://docs.gitlab.com/ee/ci/

.. _Drone CI: https://docs.drone.io/pipeline/overview/

.. _Github Actions: https://docs.github.com/en/actions
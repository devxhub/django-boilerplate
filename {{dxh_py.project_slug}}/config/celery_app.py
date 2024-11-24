import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("{{dxh_py.project_slug}}")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-db-backup-script': {
        'task': '{{dxh_py.project_slug}}.setting.tasks.run_db_backup_script',
        'schedule': crontab(minute=0, hour=0) # Execute daily at 0 AM.
    },
}

{% if dxh_py.use_celery == 'y' and dxh_py.use_docker == 'y' %}

from celery import shared_task
import subprocess

@shared_task(bind=True)
def run_db_backup_script(self):
    try:
        subprocess.run(["bash", "./db_backup.sh"], check=True)
        return "Backup completed successfully."
    except subprocess.CalledProcessError as e:
        return f"Backup failed: {e}"
    
{%- endif %}

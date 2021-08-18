from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set django settings module environment variable for the celery command line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

# atuo discover tasks.py and import those tasks for celery to run
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))
  
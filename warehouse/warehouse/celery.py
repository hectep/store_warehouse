import os

from celery import Celery
from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'warehouse'
CELERY_QUEUES = (
    Queue('warehouse', Exchange('warehouse'), routing_key='warehouse'),
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
app = Celery('warehouse', broker='pyamqp://guest@localhost//')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

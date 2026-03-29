import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "residentevil_gunshop.settings")

app = Celery("residentevil_gunshop")


app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()
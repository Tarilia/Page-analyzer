import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')


def make_celery():
    celery = Celery(
        main='page_analyzer',
        broker=CELERY_BROKER_URL,
        backend=CELERY_RESULT_BACKEND,
        include=['page_analyzer.tasks'],
    )
    return celery


celery_app = make_celery()

celery_app.conf.beat_schedule = {
    'process_urls_checks_every_minutes': {
        'task': 'page_analyzer.tasks.check_all_urls',
        'schedule': crontab(minute='*/1')
    }
}

from celery import shared_task
from django.core.mail import send_mail

from celery_progress.backend import ProgressRecorder
from time import sleep


@shared_task
def send_email_task():

    sleep(2)
    send_mail('Celery Task Worked!',
            'This is the prrof that task worked!',
            'jinjai@auauau.com',
            ['xipoy85582@estopg.com']
            )
    return None

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(100):
        sleep(duration)
        progress_recorder.set_progress(i+1, 100, f'On iteration {i}')
    return 'Done'


@shared_task(bind=True)
def sleepy(self, duration):
    sleep(duration)
    return 'Done'
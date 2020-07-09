from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

from .tasks import send_email_task,go_to_sleep,sleepy
# Create your views here.

#def index(request):
 #   send_email_task.delay()
  #  return HttpResponse('<h1> Email has been Sent with Celery! </h1>')

def index(request):
    result  = go_to_sleep.delay(1)
    return render(request, 'index.html',{'task_id' : result.task_id})
    
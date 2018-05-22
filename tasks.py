import requests
from celery import Celery

celery = Celery('polling', broker='redis://localhost:6379')

@celery.tasks
def poll():
    r = requests.get('http://localhost:8080/subscribe/test/message')
    response = r.json()

    return response['message']

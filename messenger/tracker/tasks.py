import datetime
import time
from celery import shared_task

from application import celery_app

from django.core.mail import send_mail

from users.models import User


@celery_app.task()
def send_mail_create(username, user_id, date):
    time.sleep(30)
    send_mail(
        'Django',
        f'Новый пользователь {username} c id={user_id} создан в {date} ',
        'nnonamet@yandex.ru',
        ['p.g1adyshev@yandex.ru'],
        fail_silently=False,
    )


@celery_app.task()
def count_users():
    f = open('count_users.txt', 'a+')
    tmp = User.objects.all().count()
    dt = datetime.datetime.now()
    f.write(f'{tmp} {dt} \n')
    f.close()

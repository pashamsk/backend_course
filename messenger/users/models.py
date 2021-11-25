from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя пользователя')
    nick = models.CharField(max_length=64, unique=True, verbose_name='ник пользователя')

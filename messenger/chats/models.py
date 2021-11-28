from django.db import models
from django.utils import timezone

from users.models import User


class Chat(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='название чата'
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # on_delete=models.SET_DEFAULT(?),
        verbose_name='создатель чата'
    )
    added_at = models.DateTimeField('дата создания', default=timezone.now)
    updated_at = models.DateTimeField('последнее изменение', default=timezone.now)

    class Meta:
        ordering = ('-added_at',)
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.title

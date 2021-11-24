from django.db import models

from users.models import User

class Chat(models.Model):
    chat_name = models.CharField(max_length=64, verbose_name='название чата')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='?создатель чата')
    added_at = models.DateField(verbose_name='дата создания чата')

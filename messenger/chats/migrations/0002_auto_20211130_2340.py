# Generated by Django 3.2.9 on 2021-11-30 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('-added_at',), 'verbose_name': 'чат', 'verbose_name_plural': 'чаты'},
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='user_id',
            new_name='user',
        ),
    ]
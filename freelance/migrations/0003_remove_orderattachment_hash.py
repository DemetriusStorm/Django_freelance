# Generated by Django 3.2.9 on 2021-11-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0002_orderchat_orderchatmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderattachment',
            name='hash',
        ),
    ]
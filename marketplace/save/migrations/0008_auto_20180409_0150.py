# Generated by Django 2.0.3 on 2018-04-08 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_auto_20180408_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status task'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_tech_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech',
            name='user',
        ),
        migrations.AddField(
            model_name='tech',
            name='user',
            field=models.ManyToManyField(to='main_app.User'),
        ),
    ]

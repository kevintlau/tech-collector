# Generated by Django 3.2.4 on 2021-07-18 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210718_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tech',
            old_name='user',
            new_name='users',
        ),
    ]

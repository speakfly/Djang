# Generated by Django 2.0.2 on 2018-02-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='humi',
            field=models.IntegerField(default=0),
        ),
    ]

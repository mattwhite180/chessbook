# Generated by Django 2.2.12 on 2021-05-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessapp', '0003_game_time_controls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time_controls',
            field=models.FloatField(),
        ),
    ]

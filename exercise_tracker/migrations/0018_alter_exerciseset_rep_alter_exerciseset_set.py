# Generated by Django 4.1.1 on 2022-10-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_tracker', '0017_remove_session_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='rep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='set',
            field=models.IntegerField(),
        ),
    ]

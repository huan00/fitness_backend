# Generated by Django 4.1.1 on 2022-10-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_tracker', '0016_rename_workoutset_workout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='user',
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-13 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0015_alter_workoutset_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutset',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='workoutset',
            name='workout',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
        migrations.DeleteModel(
            name='WorkoutSet',
        ),
    ]
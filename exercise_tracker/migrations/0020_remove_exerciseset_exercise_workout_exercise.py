# Generated by Django 4.1.1 on 2022-10-19 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0016_remove_workoutset_exercise_remove_workoutset_workout_and_more'),
        ('exercise_tracker', '0019_alter_session_workout_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseset',
            name='exercise',
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercise.exercise'),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_tracker', '0008_alter_workoutset_options_remove_workoutset_exercise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutset',
            name='exercise_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_set', to='exercise_tracker.exerciseset'),
        ),
        migrations.AddField(
            model_name='workoutset',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='exercise_tracker.session'),
        ),
    ]

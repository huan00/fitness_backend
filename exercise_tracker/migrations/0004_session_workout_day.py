# Generated by Django 4.1.1 on 2022-10-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_tracker', '0003_alter_workoutset_options_alter_workoutset_exercise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='workout_day',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='MON', max_length=4),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_workout_alter_exercise_options_alter_set_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='set',
            field=models.IntegerField(default=1),
        ),
    ]
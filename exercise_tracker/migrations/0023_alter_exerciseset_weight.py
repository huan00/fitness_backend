# Generated by Django 4.1.1 on 2022-10-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_tracker', '0022_alter_workout_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
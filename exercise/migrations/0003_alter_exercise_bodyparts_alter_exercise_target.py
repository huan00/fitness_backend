# Generated by Django 4.1.1 on 2022-09-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_exercise_bodyparts_exercise_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='bodyParts',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='target',
            field=models.JSONField(),
        ),
    ]
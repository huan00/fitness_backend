# Generated by Django 4.1.1 on 2022-09-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='bodyParts',
            field=models.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='target',
            field=models.JSONField(default='{}'),
        ),
    ]

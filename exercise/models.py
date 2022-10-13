from email.policy import default
from django.db import models


# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=255, default='')
    bodyParts = models.JSONField(default=list)
    gifUrl = models.CharField(max_length=255, default='')
    target = models.JSONField(default=list)
    equipment = models.JSONField(default=list)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

from django.db import models


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    bodyParts = models.JSONField()
    gifUrl = models.CharField(max_length=255)
    target = models.JSONField()

    class Meta:
      ordering = ('name',)
    
    def __str__(self):
      return self.name
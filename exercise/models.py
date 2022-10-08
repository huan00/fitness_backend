from django.db import models


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    bodyParts = models.JSONField(default=list)
    gifUrl = models.CharField(max_length=255, default='')
    target = models.JSONField(default=list)
    equipment = models.JSONField(default=list)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class set(models.Model):
    exercise = models.ForeignKey(
        Exercise, related_name='exercises', on_delete=models.CASCADE)
    rep = models.IntegerField(default=1)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('rep')

    def __str__(self):
        return self.rep

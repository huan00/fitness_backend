from django.db import models
from django.contrib.auth.models import User

from exercise.models import Exercise

# Create your models here.
# class workout(models.Model):
#   set = models.ForeignKey(Set, related_name='sets', on_delete=models.CASCADE)


class Session(models.Model):
    user = models.ForeignKey(User, related_name='session',
                             on_delete=models.CASCADE, null=True)
    workout_day = models.TextField(max_length=100)
    focus_area = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]

    def display():
        pass

    def __str__(self):
        workout_Focus = (' '.join(self.focus_area))
        return self.workout_day + " Focus- " + workout_Focus


class Workout(models.Model):
    session = models.ForeignKey(
        Session, related_name='workout', on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(
        Exercise, related_name='exercise', on_delete=models.PROTECT, null=True)
    # pull exercise from exercise
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.exercise.name


class ExerciseSet(models.Model):
    workout = models.ForeignKey(
        Workout, related_name='exercise_set', on_delete=models.CASCADE, null=True)
    set = models.IntegerField()
    rep = models.IntegerField()
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('set', )

    def __str__(self):
        return '%s' % self.set

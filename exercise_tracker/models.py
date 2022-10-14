from django.db import models
from django.contrib.auth.models import User

from exercise.models import Exercise

# Create your models here.
# class workout(models.Model):
#   set = models.ForeignKey(Set, related_name='sets', on_delete=models.CASCADE)


class Session(models.Model):
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THUR'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    day = [(MONDAY, 'Monday'), (TUESDAY, 'Tuesday'), (WEDNESDAY, 'Wednesday'), (THURSDAY,
                                                                                'Thursday'), (FRIDAY, 'Friday'), (SATURDAY, 'Saturday'), (SUNDAY, 'Sunday')]

    # user = models.ForeignKey(
    #     User, related_name='session', on_delete=models.CASCADE)
    workout_day = models.CharField(max_length=4, choices=day, default=MONDAY)
    focus_area = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.workout_day


class Workout(models.Model):
    session = models.ForeignKey(
        Session, related_name='workout', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.session.workout_day + ' workout'


class ExerciseSet(models.Model):
    exercise = models.ForeignKey(
        Exercise, related_name='exercise', on_delete=models.CASCADE, null=True)
    workout = models.ForeignKey(
        Workout, related_name='exercise_set', on_delete=models.CASCADE, null=True)
    # pull exercise from exercise
    set = models.IntegerField()
    rep = models.IntegerField()
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('set', )

    def __str__(self):
        return self.exercise.name

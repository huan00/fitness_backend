from django.contrib import admin
from .models import Session, Workout, ExerciseSet

# Register your models here.

admin.site.register(Session)
admin.site.register(Workout)
admin.site.register(ExerciseSet)

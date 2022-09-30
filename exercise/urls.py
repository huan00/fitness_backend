from django.urls import path, include
from exercise import views

urlpatterns = [
  path('exerciseslist/', views.ExerciseList.as_view())
]
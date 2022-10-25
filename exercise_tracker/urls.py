from django.urls import path
from exercise_tracker import views

urlpatterns = [
    path('saveSession/', views.saveSession),
    path('sessions', views.SessionsHistory.as_view()),
    path('saveExerciseSet/', views.saveExerciseSet),
    path('mysessionshistory/', views.SessionsHistory.as_view())
]

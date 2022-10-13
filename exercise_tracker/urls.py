from django.urls import path
from exercise_tracker import views

urlpatterns = [
    path('sessions', views.SessionsHistory.as_view())
]

from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ExerciseSerializer
from rest_framework.response import Response

# Create your views here.

from .models import Exercise

class ExerciseList(APIView):
  def get(self, request, format=None):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)

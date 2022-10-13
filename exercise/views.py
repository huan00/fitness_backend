from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ExerciseSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view
from django.http import Http404

# Create your views here.

from .models import Exercise


class ExerciseList(APIView):
    def get(self, request, format=None):
        print(Exercise.objects)
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addExercise(request):
    serializer = ExerciseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response('Hello')

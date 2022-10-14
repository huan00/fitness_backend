from django.shortcuts import render

from .models import Session
from .serializers import ExerciseSetSerializer, MySessionSerializer, SessionSerializer

from django.http import Http404

from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.


@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def saveSession(request):
    serializer = SessionSerializer(data=request.data)
    # print(serializer)

    if serializer.is_valid():  # check to make sure submitted data match serializer
        # serializer.save(user=request.user)
        serializer.save()
        try:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def saveExerciseSet(request):
    serializer = ExerciseSetSerializer(data=request.data)

    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


class SessionsHistory(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # sessions = Session.objects.filter(user=request.user)
        sessions = Session.objects.all()
        serializer = MySessionSerializer(sessions, many=True)
        return (Response(serializer.data))

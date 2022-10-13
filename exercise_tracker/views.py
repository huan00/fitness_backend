from django.shortcuts import render

from .models import Session
from .serializers import MySessionSerializer

from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class SessionsHistory(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # sessions = Session.objects.filter(user=request.user)
        sessions = Session.objects.all()
        serializer = MySessionSerializer(sessions, many=True)
        return (Response(serializer.data))

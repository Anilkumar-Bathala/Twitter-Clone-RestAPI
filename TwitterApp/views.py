from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

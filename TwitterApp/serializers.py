from .models import *
from rest_framework.serializers import ModelSerializer, Serializer


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Follower(models.Model):
    follower_id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    follower_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following_user_id = models.ManyToManyField(User, related_name='following')


class Tweet(models.Model):
    tweet_id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    tweet = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Reply(models.Model):
    reply_id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    reply = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Like(models.Model):
    like_id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


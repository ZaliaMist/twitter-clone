from django.db import models
from twitteruser.models import MyUser
from django.utils import timezone


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    my_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

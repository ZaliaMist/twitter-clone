from django.db import models
from twitteruser.models import MyUser
from tweet.models import Tweet


class Notify(models.Model):
    user_who_tagged_me = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="user_who_tagged_me")
    tagged_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="tagged_user")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet")
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.tweet.title


from django.shortcuts import render, redirect
from tweet.forms import TweetF
from tweet.models import Tweet
from twitteruser.models import MyUser
from notification.models import Notify
from django.contrib.auth.models import User
from config.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
import re



@login_required
def createtweet_view(request):
    if request.method == "POST":
        form = TweetF(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body=data["body"],
                my_user=request.user
            )
            pattern = r"@(\w{1,15})"
            pattern_matches = re.findall(pattern, data['body'])
            total_users = MyUser.objects.all()
            for person in total_users:
                if person.username in pattern_matches or person.display_name in pattern_matches:
                    Notify.objects.create(
                        user_who_tagged_me = request.user,
                        tagged_user = person,
                        tweet = new_tweet
                    )
            return redirect("/")
    form = TweetF()
    return render(request, 'createtweet.html', {"form": form})


def tweetinfo_view(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    return render(request,
    'tweetinfo.html',
    {'tweets': tweets, 
    "user_model": AUTH_USER_MODEL
    })

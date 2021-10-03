from django.shortcuts import render, redirect
from twitteruser.forms import MyUserF
from twitteruser.models import MyUser
from tweet.models import Tweet
from tweet.views import tweetinfo_view
from notification.models import Notify
from django.contrib.auth.models import User
from config.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    tweets = Tweet.objects.all().order_by('-time')
    user = request.user
    all_users = MyUser.objects.all()
    notifications = Notify.objects.filter(tagged_user=user, is_seen=False)
    num_notes = len(notifications)
    return render(request,
    'home.html',
    {'all_users': all_users, 
    'user': user,
    'notifications': notifications,
    'num_notes': num_notes,
    "user_model": AUTH_USER_MODEL, 
    "tweets": tweets
    })


def userinfo_view(request, user_id):
    user = MyUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(my_user=user.id)
    return render(request, "userinfo.html", {"user": user, "tweets": tweets})


def follow_view(request, user_id):
    user_to_follow = MyUser.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return redirect(userinfo_view, user_id=user_id)


def unfollow_view(request, user_id):
    user_to_unfollow = MyUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return redirect(userinfo_view, user_id=user_id)

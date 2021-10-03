"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import home_view, userinfo_view, follow_view, unfollow_view
from tweet.views import createtweet_view, tweetinfo_view
from authentication.views import login_view, logout_view, signup_view
from notification.views import notification_view, allusers_view


urlpatterns = [
    path('admin/', admin.site.urls),
#twitteruser
    path('', home_view, name="home"),
    path('userinfo/<int:user_id>/', userinfo_view),
    path('follow/<int:user_id>/', follow_view),
    path('unfollow/<int:user_id>/', unfollow_view),
#tweet
    path('createtweet/', createtweet_view),
    path('tweetinfo/<int:tweet_id>/', tweetinfo_view),
#authentication
    path('login/', login_view, name="login"),
    path('logout/', logout_view),
    path('signup/', signup_view),
#notification
    path('notification/<int:notification_id>/', notification_view),
    path('allusers/', allusers_view),
]

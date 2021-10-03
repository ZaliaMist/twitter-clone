from django import forms
from tweet.models import Tweet
from twitteruser.models import MyUser
 

class TweetF(forms.Form):
    body = forms.CharField(max_length=140)
    my_user = forms.ModelChoiceField(queryset=MyUser.objects.all())

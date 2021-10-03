from django import forms
from twitteruser.models import MyUser
 

class MyUserF(forms.Form):
    display_name = forms.CharField(max_length=100)


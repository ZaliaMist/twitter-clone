from django import forms
from twitteruser.models import MyUser


# login to your acct page:
class LoginForm(forms.Form):
   username = forms.CharField(max_length=150)
   password = forms.CharField(widget=forms.PasswordInput)


# signup
class AddUserForm(forms.Form):
   display_name = forms.CharField(max_length=30, required=False)
   username = forms.CharField(max_length=150)
   password = forms.CharField(widget=forms.PasswordInput)


from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from authentication.forms import LoginForm, AddUserForm
from twitteruser.models import MyUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username=data["username"],
                password=data["password"],
                display_name=data["display_name"]
            )
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
        return HttpResponseRedirect(reverse("home"))
    form = AddUserForm()
    return render(request, 'signup.html', {"form": form})


def login_view(request):
   if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           data = form.cleaned_data
           user = authenticate(
               request, username=data["username"], password=data["password"]
           )
           if user:
               login(request, user)
               return HttpResponseRedirect(
                   request.GET.get("next", reverse("home"))
               )
 
   form = LoginForm()
   return render(request, 'login.html', {"form": form})
 

@login_required
def logout_view(request):
   logout(request)
   return redirect("home")

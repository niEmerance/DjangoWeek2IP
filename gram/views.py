from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def welcome(request):
    return render(request,'welcome.html')

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(response, "all-grams/registration/register.html", {"form":form})

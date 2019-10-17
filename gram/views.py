from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import RegisterForm

def welcome(request):
    return render(request,'welcome.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('welcome')
    else:
        form = RegisterForm()
    return render(response, "all-grams/registration/register.html", {"form":form})

from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request,'welcome.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('gram:welcome')
    else:
        form = RegisterForm()
    return render(response, "all-grams/registration/register.html", {"form":form})


def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('gram:welcome')
    else:
        form=AuthenticationForm()
    return render(request, 'all-grams/registration/login.html',{"form":form})
            

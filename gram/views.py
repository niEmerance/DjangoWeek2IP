from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,NewPostForm,CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='login/')
def welcome(request):
    try:
        posts= Post.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'welcome.html',{"posts":posts})

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

@login_required(login_url='login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.upload_by = current_user
            post.save()
        return redirect('gram:welcome')

    else:
        form = NewPostForm()
    return render(request, 'all-grams/new_post.html', {"form": form})

            

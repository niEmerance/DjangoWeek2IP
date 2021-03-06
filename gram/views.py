from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import RegisterForm,NewPostForm,CommentForm,UserUpdateForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Profile
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

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect('gram:login')

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

def like_post(request):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('gram:welcome')

def unlike_post(request):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    post.unlikes.add(request.user)
    return redirect('gram:welcome')

@login_required(login_url='login/')
def profile(request):
    profiles= Profile.objects.all()
    return render(request,'all-grams/profile.html',{"profiles":profiles})

@login_required(login_url='login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.all()
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')
    return render(request,'all-grams/edit_profile.html',locals())
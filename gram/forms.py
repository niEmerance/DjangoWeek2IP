from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment


class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
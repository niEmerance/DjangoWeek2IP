from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment,Profile


class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date']

# class ProfileForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['fullname'].widget=forms.TextInput()
#    class Meta:
#        model=Profile
#        exclude=['username']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=['profile_pic']
class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['bio'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['username']
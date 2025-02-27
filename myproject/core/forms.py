from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter Username"
        })
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter Email"
        })
    )

    first_name = forms.CharField(
        required=True,
        label="First Name",
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "First Name"
        })
    )

    last_name = forms.CharField(
        required=True,
        label="Last Name",
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Last Name"
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Password"
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-md focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Re-enter ur password"
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
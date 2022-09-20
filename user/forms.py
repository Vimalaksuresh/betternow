from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


USER = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = USER
        fields = ["email", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
   


# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = USER
#         fields = ["username", "password"]

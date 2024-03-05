from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(widget= forms.PasswordInput(attrs= {"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs= {"class": "form-control", "placeholder": "Retype Password"}))
    class Meta:
        model = User
        fields = ['phone_number', 'username']
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "username"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "+998123456789"
            })
        }

class LoginForm(forms.Form):
    password = forms.CharField(widget= forms.PasswordInput(attrs= {"class": "form-control", "placeholder": "Password"}))
    username = forms.CharField(widget= forms.TextInput(attrs= {"class": "form-control", "placeholder": "Username"}))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    cargo = forms.CharField(max_length=100, help_text='Cargo del Usuario')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "cargo"]

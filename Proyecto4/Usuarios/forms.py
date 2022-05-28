from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeticionRegistro(UserCreationForm):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    DNI = forms.IntegerField(label='DNI')
    direccion = forms.CharField(max_length=60, required=False)
    telefono = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    profesorado = forms.CharField(max_length=40, required=True)
    cargo = forms.CharField(max_length=40, required=True)
    username = forms.CharField(label='Nombre de usuario', help_text='')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='La contraseña debe de tener al menos 8 carácteres y no debe de ser similar a tu nombre de usuario o estar hecha totalmente por números.')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = {k: '' for k in fields}


from django import forms
from django.forms import ModelForm
from .models import Curso, Nota

class Alumnoform(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'apellido', 'DNI', 'direccion', 'telefono', 'email', 'curso']

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    DNI = forms.IntegerField()
    telefono = forms.IntegerField()
    direccion = forms.CharField(max_length=60)
    email = forms.EmailField()
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())

class Notaform(ModelForm):
    class Meta:
        model = Nota
        fields = ['C1', 'C2', 'C3']

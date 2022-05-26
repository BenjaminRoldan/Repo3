from django import forms
from django.forms import ModelForm
from .models import Curso

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

class DocentesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    edad = forms.IntegerField()
    especialidad = forms.CharField()

class CursoFormulario(forms.Form):

    materia = forms.CharField()
    nivel = forms.CharField()

class MateriaFormulario(forms.Form):

    nombre = forms.CharField()
    nivel = forms.CharField()

class PersLimpFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    turno = forms.CharField()
from django import forms

class AutoridadesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    cargo = forms.CharField()

class AlumnosFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    edad = forms.IntegerField()

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
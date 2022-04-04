from django import forms

class InstitucionFormulario(forms.Form):

    nombre = forms.CharField()
    direccion = forms.CharField()
    nivel = forms.CharField()

class AdministrativosFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()

class DocentesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    materia = forms.CharField()

class PersonalLimpiezaFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    turno = forms.CharField()
from django import forms

class InstitucionFormulario(forms.Form):

    nombre = forms.CharField()
    direccion = forms.CharField()
    nivel = forms.CharField()
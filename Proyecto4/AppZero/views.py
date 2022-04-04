from django.shortcuts import render
from AppZero.forms import *
from AppZero.models import *

# Create your views here.

def inicio(request):

    return render(request, "AppZero/inicio.html")

def instituciones(request):

    return render(request, "AppZero/instituciones.html")

def administrativos(request):

    return render(request, "AppZero/administrativos.html")

def docentes(request):

    return render(request,"AppZero/docentes.html")

def personalLimpieza(request):

    return render(request, "AppZero/personalLimpieza.html")

def institucionFormulario(request):

    if request.method == 'POST':

        instFormulario = InstitucionFormulario(request.POST)

        print(instFormulario)

        if instFormulario.is_valid:

            informacion = instFormulario.cleaned_data

            institucion = Institucion (nombre=informacion['nombre'], direccion=informacion['direccion'], nivel=informacion['nivel'])

            institucion.save()

            return render(request, "AppZero/inicio.html")

    else:

        instFormulario = InstitucionFormulario()

    
    return render (request, "AppZero/institucionFormulario.html", {"instFormulario":instFormulario})

def busquedaInstitucion(request):

    return render(request, 'AppZero/busquedaInstitucion.html')

def buscarInstitucion(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Institucion.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarInstitucion.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})


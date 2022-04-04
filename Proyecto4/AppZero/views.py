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

def administrativosFormulario(request):

    if request.method == 'POST':

        admonFormulario = AdministrativosFormulario(request.POST)

        print(admonFormulario)

        if admonFormulario.is_valid:

            informacion = admonFormulario.cleaned_data

            administrativo = Administrativo (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])

            administrativo.save()

            return render(request, "AppZero/inicio.html")

    else:

        admonFormulario = AdministrativosFormulario()

    
    return render (request, "AppZero/administrativosFormulario.html", {"admonFormulario":admonFormulario})

def busquedaAdministrativos(request):

    return render(request, 'AppZero/busquedaAdministrativos.html')

def buscarAdministrativos(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Administrativo.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarAdministrativos.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def docentesFormulario(request):

    if request.method == 'POST':

        docFormulario = DocentesFormulario(request.POST)

        print(docFormulario)

        if docFormulario.is_valid:

            informacion = docFormulario.cleaned_data

            docentes = Docente (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], materia=informacion['materia'])

            docentes.save()

            return render(request, "AppZero/inicio.html")

    else:

        docFormulario = DocentesFormulario()

    
    return render (request, "AppZero/docentesFormulario.html", {"docFormulario":docFormulario})

def busquedaDocentes(request):

    return render(request, 'AppZero/busquedaDocentes.html')

def buscarDocentes(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Docente.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarDocentes.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def personalLimpiezaFormulario(request):

    if request.method == 'POST':

        perslimpFormulario = PersonalLimpiezaFormulario(request.POST)

        print(perslimpFormulario)

        if perslimpFormulario.is_valid:

            informacion = perslimpFormulario.cleaned_data

            persLimpieza = PersonalLimpieza (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], turno=informacion['turno'])

            persLimpieza.save()

            return render(request, "AppZero/inicio.html")

    else:

        perslimpFormulario = PersonalLimpiezaFormulario()

    
    return render (request, "AppZero/personalLimpiezaFormulario.html", {"perslimpFormulario":perslimpFormulario})

def busquedaPersonalLimpieza(request):

    return render(request, 'AppZero/busquedaPersonalLimpieza.html')

def buscarPersonalLimpieza(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = PersonalLimpieza.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarPersonalLimpieza.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

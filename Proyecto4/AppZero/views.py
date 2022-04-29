from django.shortcuts import render
from AppZero.forms import *
from AppZero.models import *

# Create your views here.

def inicio(request):

    return render(request, "AppZero/inicio.html")

def autoridades(request):

    return render(request, "AppZero/autoridades.html")

def alumnos(request):

    return render(request, "AppZero/alumnos.html")

def profesores(request):

    return render(request,"AppZero/profesores.html")

def cursos(request):

    return render(request, "AppZero/cursos.html")

def materias(request):

    return render(request, "AppZero/materias.html")

def autoridadFormulario(request):

    if request.method == 'POST':

        autFormulario = AutoridadesFormulario(request.POST)

        print(autFormulario)

        if autFormulario.is_valid:

            informacion = autFormulario.cleaned_data

            autoridad = Autoridad (nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], cargo=informacion['cargo'])

            autoridad.save()

            return render(request, "AppZero/inicio.html")

    else:

        autFormulario = AutoridadesFormulario()

    
    return render (request, "AppZero/autoridadFormulario.html", {"autFormulario":autFormulario})

def busquedaAutoridad(request):

    return render(request, 'AppZero/busquedaAutoridad.html')

def buscarAutoridad(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Autoridad.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarAutoridad.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def alumnosFormulario(request):

    if request.method == 'POST':

        alumnoFormulario = AlumnosFormulario(request.POST)

        print(alumnoFormulario)

        if alumnoFormulario.is_valid:

            informacion = alumnoFormulario.cleaned_data

            alumnos = Alumno (nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], edad=informacion['edad'])

            alumnos.save()

            return render(request, "AppZero/inicio.html")

    else:

        alumnoFormulario = AlumnosFormulario()

    
    return render (request, "AppZero/alumnosFormulario.html", {"alumnoFormulario":alumnoFormulario})

def busquedaAlumnos(request):

    return render(request, 'AppZero/busquedaAlumnos.html')

def buscarAlumnos(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Alumno.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadobuscarAlumnos.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def profesoresFormulario(request):

    if request.method == 'POST':

        profeFormulario = ProfesoresFormulario(request.POST)

        print(profeFormulario)

        if profeFormulario.is_valid:

            informacion = profeFormulario.cleaned_data

            profesores = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], edad=informacion['edad'], especialidad=informacion['especialidad'])

            profesores.save()

            return render(request, "AppZero/inicio.html")

    else:

        profeFormulario = ProfesoresFormulario()

    
    return render (request, "AppZero/profesoresFormulario.html", {"profeFormulario":profeFormulario})

def busquedaProfesores(request):

    return render(request, 'AppZero/busquedaProfesores.html')

def buscarProfesores(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Profesor.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarProfesores.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def cursoFormulario(request):

    if request.method == 'POST':

        curFormulario = CursoFormulario(request.POST)

        print(curFormulario)

        if curFormulario.is_valid:

            informacion = curFormulario.cleaned_data

            cur = Curso (materia=informacion['materia'], nivel=informacion['nivel'])

            cur.save()

            return render(request, "AppZero/inicio.html")

    else:

        curFormulario = CursoFormulario()

    
    return render (request, "AppZero/cursoFormulario.html", {"curFormulario":curFormulario})

def busquedaCurso(request):

    return render(request, 'AppZero/busquedaCurso.html')

def buscarCurso(request):

    if request.GET["materia"]:

        materia = request.GET['materia']
        materias = Curso.objects.filter(materia=materia)

        return render(request, "AppZero/resultadoBuscarCurso.html", {"materias":materias, "materia":materia})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})

def materiaFormulario(request):

    if request.method == 'POST':

        materFormulario = MateriaFormulario(request.POST)

        print(materFormulario)

        if materFormulario.is_valid:

            informacion = materFormulario.cleaned_data

            materias = Materia (nombre=informacion['nombre'], nivel=informacion['nivel'])

            materias.save()

            return render(request, "AppZero/inicio.html")

    else:

        materFormulario = MateriaFormulario()

    
    return render (request, "AppZero/materiaFormulario.html", {"materFormulario":materFormulario})

def busquedaMateria(request):

    return render(request, 'AppZero/busquedaMateria.html')

def buscarMateria(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        nombres = Materia.objects.filter(nombre=nombre)

        return render(request, "AppZero/resultadoBuscarMateria.html", {"nombres":nombres, "nombre":nombre})

    else:

        respuesta = "No se colocaron datos"


    return render(request, "AppZero/inicio.html", {"respuesta":respuesta})
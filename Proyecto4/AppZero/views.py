from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import render
from AppZero.forms import *
from AppZero.models import *
from .forms import Alumnoform
from django.views import View


def inicio(request):
    return render(request, "AppZero/inicio.html")

def vergrados(request):
    return render(request, "AppZero/Cursos/viewgrados.html")

def vercursos(request, id):
    if id == '1A':
        alumnos = Alumno.objects.filter(curso__grado=1).filter(curso__division='A')
    if id == '1B':
        alumnos = Alumno.objects.filter(curso__grado=1).filter(curso__division='B')
    if id == '2A':
        alumnos = Alumno.objects.filter(curso__grado=2).filter(curso__division='A')
    if id == '2B':
        alumnos = Alumno.objects.filter(curso__grado=2).filter(curso__division='B')
    if id == '3A':
        alumnos = Alumno.objects.filter(curso__grado=3).filter(curso__division='A')
    if id == '3B':
        alumnos = Alumno.objects.filter(curso__grado=3).filter(curso__division='B')
    if id == '4A':
        alumnos = Alumno.objects.filter(curso__grado=4).filter(curso__division='A')
    if id == '4B':
        alumnos = Alumno.objects.filter(curso__grado=4).filter(curso__division='B')
    if id == '5A':
        alumnos = Alumno.objects.filter(curso__grado=5).filter(curso__division='A')
    if id == '5B':
        alumnos = Alumno.objects.filter(curso__grado=5).filter(curso__division='B')
    if id == '6A':
        alumnos = Alumno.objects.filter(curso__grado=6).filter(curso__division='A')
    if id == '6B':
        alumnos = Alumno.objects.filter(curso__grado=6).filter(curso__division='B')
    return render(request, "AppZero/Cursos/viewcursos.html", {'alumnos': alumnos})

def buscarAlumnoDNI(request):

    dni = request.GET.get('dni')
    if dni is not None:
        try:
            alumno = Alumno.objects.get(DNI=dni)
            
            try:
                prom1 = (alumno.calificaciones.matematicas.C1 + alumno.calificaciones.cienciasnaturales.C1 + 
                alumno.calificaciones.cienciassociales.C1 + alumno.calificaciones.practlenguaje.C1 + 
                alumno.calificaciones.ingles.C1 + alumno.calificaciones.educacionfisica.C1) / 6
                prom1 = round(prom1, 2)
            except:
                prom1 = None

            try:
                prom2 = (alumno.calificaciones.matematicas.C2 + alumno.calificaciones.cienciasnaturales.C2 + 
                alumno.calificaciones.cienciassociales.C2 + alumno.calificaciones.practlenguaje.C2 + 
                alumno.calificaciones.ingles.C2 + alumno.calificaciones.educacionfisica.C2) / 6
                prom2 = round(prom2, 2)
            except:
                prom2 = None

            try:
                prom3 = (alumno.calificaciones.matematicas.C3 + alumno.calificaciones.cienciasnaturales.C3 + 
                alumno.calificaciones.cienciassociales.C3 + alumno.calificaciones.practlenguaje.C3 + 
                alumno.calificaciones.ingles.C3 + alumno.calificaciones.educacionfisica.C3) / 6
                prom3 = round(prom3, 2)
            except:
                prom3 = None
        except: 
            return render(request, "AppZero/Alumnos/buscaralumnodni.html", {'error': 1})
    else:
        alumno = ''
        prom1, prom2, prom3 = None, None, None
    return render(request, "AppZero/Alumnos/buscaralumnodni.html", {'alumno': alumno, 'prom1': prom1, 'prom2': prom2, 'prom3': prom3})


################## CRUD Alumnos ##################
class AlumnosList(ListView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_list.html'

class AlumnosDetail(DetailView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_detail.html'
    
class AlumnosCreate(CreateView):
    model = Alumno
    success_url = '/AppZero/grados/'
    fields = ['nombre', 'apellido', 'DNI', 'direccion', 'telefono', 'email', 'curso']

class AlumnosUpdate(UpdateView):
    model = Alumno
    success_url = '/AppZero/alumnos/lista'
    fields = '__all__'

class AlumnosDelete(DeleteView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_confirm_delete.html'
    success_url = '/AppZero/alumnos/lista'
##################################################################



################## CRUD Docentes ##################
class DocentesList(ListView):
    model = Docente
    template_name = 'AppZero/Docentes/docentes_list.html'

class DocentesDetail(DetailView):
    model = Docente
    template_name = 'AppZero/Docentes/docentes_detail.html'
    
class DocentesCreate(CreateView):
    model = Docente
    success_url = '/AppZero/docentes/lista'
    fields = '__all__'

class DocentesUpdate(UpdateView):
    model = Docente
    success_url = '/AppZero/docentes/lista'
    fields = '__all__'

class DocentesDelete(DeleteView):
    model = Docente
    template_name = 'AppZero/Docentes/docentes_confirm_delete.html'
    success_url = '/AppZero/docentes/lista'
##################################################################



################## CRUD Personal de limpieza ##################
class PersLimpList(ListView):
    model = PersLimp
    template_name = 'AppZero/PersLimp/perslimp_list.html'

class PersLimpDetail(DetailView):
    model = PersLimp
    template_name = 'AppZero/PersLimp/perslimp_detail.html'
    
class PersLimpCreate(CreateView):
    model = PersLimp
    success_url = '/AppZero/personal_limpieza/lista'
    fields = '__all__'

class PersLimpUpdate(UpdateView):
    model = PersLimp
    success_url = '/AppZero/personal_limpieza/lista'
    fields = '__all__'

class PersLimpDelete(DeleteView):
    model = PersLimp
    template_name = 'AppZero/PersLimp/perslimp_confirm_delete.html'
    success_url = '/AppZero/personal_limpieza/lista'
##################################################################


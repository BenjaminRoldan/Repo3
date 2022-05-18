from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import render
from AppZero.forms import *
from AppZero.models import *

def inicio(request):

    return render(request, "AppZero/inicio.html")

def buscarAlumnoDNI(request):

    dni = request.GET.get('dni')
    if dni is not None:
        try:
            alumno = Alumno.objects.get(DNI=dni)
        except: 
            return render(request, "AppZero/Alumnos/buscaralumnodni.html", {'error': 1})
    else:
        alumno = ''
    return render(request, "AppZero/Alumnos/buscaralumnodni.html", {'alumno': alumno})


################## CRUD Alumnos ##################
class AlumnosList(ListView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_list.html'

class AlumnosDetail(DetailView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_detail.html'
    
class AlumnosCreate(CreateView):
    model = Alumno
    success_url = '/AppZero/alumnos/lista'
    fields = '__all__'

class AlumnosUpdate(UpdateView):
    model = Alumno
    success_url = '/AppZero/alumnos/lista'
    fields = '__all__'

class AlumnosDelete(DeleteView):
    model = Alumno
    template_name = 'AppZero/Alumnos/alumnos_confirm_delete.html'
    success_url = '/AppZero/alumnos/lista'
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
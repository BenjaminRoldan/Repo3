from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Autoridad)

admin.site.register(Alumno)

admin.site.register(Docente)

admin.site.register(Curso)

admin.site.register(Materia)

admin.site.register(Calificacion)

admin.site.register(Grado)
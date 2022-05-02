from django.contrib import admin

from Usuarios.models import UserProfile
from .models import *

# Register your models here.

admin.site.register(Autoridad)

admin.site.register(Alumno)

admin.site.register(Profesor)

admin.site.register(Curso)

admin.site.register(Materia)

admin.site.register(UserProfile)
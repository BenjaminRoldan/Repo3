from django.contrib import admin

from Usuarios.models import UserProfile
from .models import *

# Register your models here.

admin.site.register(Institucion)

admin.site.register(Administrativo)

admin.site.register(Docente)

admin.site.register(PersonalLimpieza)

admin.site.register(UserProfile)
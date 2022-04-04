from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('instituciones', views.instituciones, name="Instituciones"),
    path('administrativos', views.administrativos, name="Administrativos"),
    path('docentes', views.docentes, name="Docentes"),
    path('personalLimpieza', views.personalLimpieza, name="Personal_de_limpieza"),
]
from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('instituciones/', views.instituciones, name="Instituciones"),
    path('administrativos/', views.administrativos, name="Administrativos"),
    path('docentes/', views.docentes, name="Docentes"),
    path('personalLimpieza/', views.personalLimpieza, name="Personal_de_limpieza"),
    path('institucionFormulario/', views.institucionFormulario, name="InstitucionFormulario"),
    path('busquedaInstitucion/', views.busquedaInstitucion, name="BusquedaInstitucion"),
    path('buscarInstitucion/', views.buscarInstitucion, name="BuscarInstitucion"),
    path('administrativosFormulario/', views.administrativosFormulario, name="AdministrativosFormulario"),
    path('busquedaAdministrativos/', views.busquedaAdministrativos, name="BusquedaAdministrativos"),
    path('buscarAdministrativos/', views.buscarAdministrativos, name="BuscarAdministrativos"),
    path('docentesFormulario/', views.docentesFormulario, name="DocentesFormulario"),
    path('busquedaDocentes/', views.busquedaDocentes, name="BusquedaDocentes"),
    path('buscarDocentes/', views.buscarDocentes, name="BuscarDocentes"),
    path('personalLimpiezaFormulario/', views.personalLimpiezaFormulario, name="PersonalLimpiezaFormulario"),
    path('busquedaPersonalLimpieza/', views.busquedaPersonalLimpieza, name="BusquedaPersonalLimpieza"),
    path('buscarPersonalLimpieza/', views.buscarPersonalLimpieza, name="BuscarPersonalLimpieza"),
]
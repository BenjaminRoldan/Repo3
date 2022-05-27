from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('', views.inicio, name="Cursos"),
    path('', views.inicio, name="Autoridades"),

    #----------------ALUMNOS----------------
    path('buscarAlumnoDNI/', views.buscarAlumnoDNI, name="BuscarAlumnoDNI"),

    path('alumnos/lista', views.AlumnosList.as_view(), name="AlumnosList"),
    path('alumnos/detalle/<pk>', views.AlumnosDetail.as_view(), name="AlumnosDetail"),
    path('alumnos/crear', views.AlumnosCreate.as_view(), name="AlumnosCreate"),
    path('alumnos/editar/<pk>', views.AlumnosUpdate.as_view(), name="AlumnosUpdate"),
    path('alumnos/borrar/<pk>', views.AlumnosDelete.as_view(), name="AlumnosDelete"),


    #---------------- DOCENTES ----------------
    path('docentes/lista', views.DocentesList.as_view(), name="DocentesList"),
    path('docentes/detalle/<pk>', views.DocentesDetail.as_view(), name="DocentesDetail"),
    path('docentes/crear', views.DocentesCreate.as_view(), name="DocentesCreate"),
    path('docentes/editar/<pk>', views.DocentesUpdate.as_view(), name="DocentesUpdate"),
    path('docentes/borrar/<pk>', views.DocentesDelete.as_view(), name="DocentesDelete"),

    #----------------PERSONAL LIMPIEZA----------------
    path('personal_limpieza/lista', views.PersLimpList.as_view(), name="PersLimpList"),
    path('personal_limpieza/detalle/<pk>', views.PersLimpDetail.as_view(), name="PersLimpDetail"),
    path('personal_limpieza/crear', views.PersLimpCreate.as_view(), name="PersLimpCreate"),
    path('personal_limpieza/editar/<pk>', views.PersLimpUpdate.as_view(), name="PersLimpUpdate"),
    path('personal_limpieza/borrar/<pk>', views.PersLimpDelete.as_view(), name="PersLimpDelete"),

    #---------------- Autoridades ----------------
    path('autoridades/lista', views.AutoridadesList.as_view(), name="AutoridadesList"),
    path('autoridades/detalle/<pk>', views.AutoridadesDetail.as_view(), name="AutoridadesDetail"),
    path('autoridades/crear', views.AutoridadesCreate.as_view(), name="AutoridadesCreate"),
    path('autoridades/editar/<pk>', views.AutoridadesUpdate.as_view(), name="AutoridadesUpdate"),
    path('autoridades/borrar/<pk>', views.AutoridadesDelete.as_view(), name="AutoridadesDelete"),

    #---------------- Cursos ----------------
    path('grados/', views.vergrados, name="VerGrados"),
    path('curso/<id>', views.vercursos, name="VerCurso"),
    path('notas/<id>', views.VerNotas, name="VerNotas"),
    path('modificar_nota/<id>/<materia>', views.EditarNota, name="ModNota"),
]

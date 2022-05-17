from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),

    #----------------ALUMNOS----------------
    path('alumnos/', views.alumnos, name="Alumnos"),
    path('alumnosFormulario/', views.alumnosFormulario, name="AlumnosFormulario"),
    path('busquedaAlumnos/', views.busquedaAlumnos, name="BusquedaAlumnos"),
    path('buscarAlumnos/', views.buscarAlumnos, name="BuscarAlumnos"),
    path('buscarAlumnoDNI/', views.buscarAlumnoDNI, name="BuscarAlumnoDNI"),


    #----------------PROFESORES----------------
    path('profesores/', views.profesores, name="Docentes"),
    path('profesoresFormulario/', views.profesoresFormulario, name="ProfesoresFormulario"),
    path('busquedaProfesores/', views.busquedaProfesores, name="BusquedaProfesores"),
    path('buscarProfesores/', views.buscarProfesores, name="BuscarProfesores"),


    #----------------AUTORIDADES----------------
    path('autoridades/', views.autoridades, name="Autoridades"),
    path('busquedaAutoridad/', views.busquedaAutoridad, name="BusquedaAutoridad"),
    path('buscarAutoridad/', views.buscarAutoridad, name="BuscarAutoridad"),
    path('autoridadFormulario/', views.autoridadFormulario, name="AutoridadFormulario"),


    #----------------CURSOS----------------
    path('cursos/', views.cursos, name="Cursos"),
    path('cursoFormulario/', views.cursoFormulario, name="CursoFormulario"),
    path('busquedaCurso/', views.busquedaCurso, name="BusquedaCurso"),
    path('buscarCurso/', views.buscarCurso, name="BuscarCurso"),


    #----------------MATERIAS----------------
    path('materias/', views.materias, name="Materias"),
    path('materiaFormulario/', views.materiaFormulario, name="MateriaFormulario"),
    path('busquedaMateria/', views.busquedaMateria, name="BusquedaMateria"),
    path('buscarMateria/', views.buscarMateria, name="BuscarMateria"),

    #----------------PERSONAL LIMPIEZA----------------
    path('personal_limpieza/lista', views.PersLimpList.as_view(), name="PersLimpList"),
    path('personal_limpieza/detalle/<pk>', views.PersLimpDetail.as_view(), name="PersLimpDetail"),
    path('personal_limpieza/crear', views.PersLimpCreate.as_view(), name="PersLimpCreate"),
    path('personal_limpieza/editar/<pk>', views.PersLimpUpdate.as_view(), name="PersLimpUpdate"),
    path('personal_limpieza/borrar/<pk>', views.PersLimpDelete.as_view(), name="PersLimpDelete"),

]
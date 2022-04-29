from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autoridades/', views.autoridades, name="Autoridades"),
    path('profesores/', views.profesores, name="Profesores"),
    path('alumnos/', views.alumnos, name="Alumnos"),
    path('cursos/', views.cursos, name="Cursos"),
    path('materias/', views.materias, name="Materias"),
    path('autoridadFormulario/', views.autoridadFormulario, name="AutoridadFormulario"),
    path('busquedaAutoridad/', views.busquedaAutoridad, name="BusquedaAutoridad"),
    path('buscarAutoridad/', views.buscarAutoridad, name="BuscarAutoridad"),
    path('alumnosFormulario/', views.alumnosFormulario, name="AlumnosFormulario"),
    path('busquedaAlumnos/', views.busquedaAlumnos, name="BusquedaAlumnos"),
    path('buscarAlumnos/', views.buscarAlumnos, name="BuscarAlumnos"),
    path('profesoresFormulario/', views.profesoresFormulario, name="ProfesoresFormulario"),
    path('busquedaProfesores/', views.busquedaProfesores, name="BusquedaProfesores"),
    path('buscarProfesores/', views.buscarProfesores, name="BuscarProfesores"),
    path('cursoFormulario/', views.cursoFormulario, name="CursoFormulario"),
    path('busquedaCurso/', views.busquedaCurso, name="BusquedaCurso"),
    path('buscarCurso/', views.buscarCurso, name="BuscarCurso"),
    path('materiaFormulario/', views.materiaFormulario, name="MateriaFormulario"),
    path('busquedaMateria/', views.busquedaMateria, name="BusquedaMateria"),
    path('buscarMateria/', views.buscarMateria, name="BuscarMateria"),
]
from django.urls import path

from AppZero import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('', views.inicio, name="Cursos"),
    path('', views.inicio, name="Docentes"),
    path('', views.inicio, name="Autoridades"),

    #----------------ALUMNOS----------------
    path('buscarAlumnoDNI/', views.buscarAlumnoDNI, name="BuscarAlumnoDNI"),

    path('alumnos/lista', views.AlumnosList.as_view(), name="AlumnosList"),
    path('alumnos/detalle/<pk>', views.AlumnosDetail.as_view(), name="AlumnosDetail"),
    path('alumnos/crear', views.AlumnosCreate.as_view(), name="AlumnosCreate"),
    path('alumnos/editar/<pk>', views.AlumnosUpdate.as_view(), name="AlumnosUpdate"),
    path('alumnos/borrar/<pk>', views.AlumnosDelete.as_view(), name="AlumnosDelete"),



    #----------------PERSONAL LIMPIEZA----------------
    path('personal_limpieza/lista', views.PersLimpList.as_view(), name="PersLimpList"),
    path('personal_limpieza/detalle/<pk>', views.PersLimpDetail.as_view(), name="PersLimpDetail"),
    path('personal_limpieza/crear', views.PersLimpCreate.as_view(), name="PersLimpCreate"),
    path('personal_limpieza/editar/<pk>', views.PersLimpUpdate.as_view(), name="PersLimpUpdate"),
    path('personal_limpieza/borrar/<pk>', views.PersLimpDelete.as_view(), name="PersLimpDelete"),

]
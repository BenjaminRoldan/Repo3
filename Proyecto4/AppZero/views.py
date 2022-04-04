from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "AppZero/inicio.html")

def instituciones(request):

    return render(request, "AppZero/instituciones.html")

def administrativos(request):

    return render(request, "AppZero/administrativos.html")

def docentes(request):

    return render(request,"AppZero/docentes.html")

def personalLimpieza(request):

    return render(request, "AppZero/personalLimpieza.html")
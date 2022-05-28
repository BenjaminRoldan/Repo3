from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import PeticionRegistro

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
        return render(request, 'inicio.html')

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request, id):
    regis = 0
    car = None

    if request.method == 'POST':
        form1 = PeticionRegistro(request.POST)
        
        if form1.is_valid():
            if id == 2:
                form1.cargo = 'Preceptor'
            elif id == 3:
                form1.cargo = 'Recursos Humanos'
            form1.save()
            return render(request, 'inicio.html')

    else:
        form1 = PeticionRegistro()
        if id == '1':
            car = 'Docente'
            regis = 1
        elif id == '2':
            car = 'Preceptor'
            regis = 2
        elif id == '3':
            car = 'Recursos Humanos'
            regis = 3
    
    return render(request, 'registro.html', {'form1': form1, 'tiporegistro': regis, 'Cargo': car})
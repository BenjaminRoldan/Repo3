from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'inicio.html', {'mensaje': f'Error, datos incorrectos'})
        else:
            return render(request, 'inicio.html', {'mensaje': f'Error, formulario erroneo'})

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {'mensaje': 'Usuario Creado'})

    else: 
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})
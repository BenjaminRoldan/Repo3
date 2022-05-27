from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html')

    else: 
        form = UserCreationForm()
        if id != '0':
            regis = True
        else:
            regis = False
    
    return render(request, 'registro.html', {'form': form, 'tiporegistro': regis})
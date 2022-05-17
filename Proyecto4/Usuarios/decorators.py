from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Inicio')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def personal_permitido(cargo_permitido=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
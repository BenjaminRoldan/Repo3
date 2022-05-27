from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('registro/<id>', views.register, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),

]
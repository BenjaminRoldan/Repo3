from django.contrib import admin
from django.urls import path,include
import AppZero.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppZero.views.inicio, name="Inicio"),
    path('AppZero/', include('AppZero.urls')),
    path('Usuarios/', include('Usuarios.urls')),
    path('Blog/', include('Blog.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

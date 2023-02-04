"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Proyecto1.views import inicio,sobreNosotros,entrar,ingresoPagina,pagina,eliminarPagina,registro,salir,perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('static/', admin.site.urls),
    path('', inicio, name= 'inicio'),
    path('sobreNosotros', sobreNosotros),
    path('ingresoPagina',ingresoPagina),
    path(r'pagina/<int:id>',pagina, name='pagina'), 
    path(r'eliminarPagina/<int:id>',eliminarPagina, name='pagina'), 
    path('entrar', entrar , name='entrar'),
    path('salir', salir, name='salir'),
    path('perfil', perfil, name='perfil'),
    path('registro', registro, name='registro'),
]
 
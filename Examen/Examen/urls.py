"""Examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Exm.views import inicio,altura,peso,color,velocidad,bv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',inicio, name="Index"),
    path('Altura',altura, name="Altura"),
    path('Peso',peso, name="Peso"),
    path('Color',color, name="Color"),
    path('Velocidad',velocidad, name="Velocidad"),
    path('Bienvenido',bv, name="Bienvenida"),

]

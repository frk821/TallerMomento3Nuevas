"""config URL Configuration

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

from web.views import Home,PlatosVista,EmpleadosVista,PlatosRegistrados,EmpleadosRegistrados #importamos la funcion "Home" de la carpeta "web" y del archivo "views"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'), #ruta que llama a la funcion Home
    path('platos/',PlatosVista, name='platos'), #ruta que llama a la funcion Platos
    path('empleados/', EmpleadosVista, name='empleados'), #ruta que llama a la funcion Empleados
    path('platosRegistrados/', PlatosRegistrados, name='platosRegistrados'),
    path('empleadosRegistrados/', EmpleadosRegistrados, name='empleadosRegistrados') 
]

"""proyectocoder URL Configuration

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
from django.urls import path, include

# from proyectocoder.views import vista_saludo
# from proyectocoder.views import inicio_sesion
# from proyectocoder.views import dia_hoy
# from proyectocoder.views import axno_nacimiento
# from proyectocoder.views import vista_plantilla1
from proyectocoder.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('saludo/', vista_saludo),
    #path('login/', inicio_sesion),
    #path('date_today/<nombre>/', dia_hoy),
    #path('año-nacimiento/<edad>/', axno_nacimiento),
    #path('home/', vista_plantilla1),
    #path('alumnos/', vista_alumnos),
    #path('alumnos2/', vista_alumnos_2),

    path("coder/", include("appcoder.urls"))
]

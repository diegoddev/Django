from django.urls import path
from proyectocoder.views import *
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", cursos),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("entregables/", entregables)
]
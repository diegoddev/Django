from django.urls import path
from proyectocoder.views import *

urlpatterns = [
    path("cursos/", cursos),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("entregables/", entregables)
]
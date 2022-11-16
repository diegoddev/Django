from django.urls import path
from proyectocoder.views import *
from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name = "coder-inicio"),
    path("cursos/", cursos, name = "coder-cursos"),
    path("estudiantes/", estudiantes, name = "coder-estudiantes"),
    path("profesores/", profesores, name = "coder-profesores"),
    path("entregables/", entregables, name = "coder-entregables")
]
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return HttpResponse("Estas en cursos")

def estudiantes(request):
    return HttpResponse("Estas en estudiantes")

def profesores(request):
    return HttpResponse("Estas en profesores")

def entregables(request):
    return HttpResponse("Estas en entregables")
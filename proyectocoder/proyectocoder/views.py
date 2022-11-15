from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba</p>""")
    
def inicio_sesion(request):
    return HttpResponse("Ingrese usuario y contraseña para iniciar sesión")

def dia_hoy(request, nombre):
    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def axno_nacimiento(request, edad):
    edad = int(edad)
    axno_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en el año {axno_nac}")

def vista_plantilla1(request):
    
    #archivo = open("./templates/template1.html") pendiente
    #abrimos archivo
    archivo = open(r"C:\Users\ddelfino004\Desktop\Django\proyectocoder\proyectocoder\templates\template1.html")
    #creamos objeto plantilla y luego cerramos el archivo para liberar recursos
    
    plantilla = Template(archivo.read())
    archivo.close()

    #Diccionario con datos para la plantilla
    datos = {"nombre": "Diego", "apellido": "Delfino", "fecha": datetime.now()}

    #Creamos contexto
    contexto = Context(datos)
    
    #Renderizamos la palntilla para crear la respuesta
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_alumnos(request):

    archivo = open(r"C:\Users\ddelfino004\Desktop\Django\proyectocoder\proyectocoder\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())
    archivo.close()

    listado_alumnos = ["Diego Delfino", "Ezequiel Delfino", "Daniel Davila", "Pedro Urquiola", "Lionel Messi", "Luis Suarez"]
    datos = {"tecnologia": "Rengoku", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_alumnos_2(request):
    
    listado_alumnos = ["Diego Delfino", "Ezequiel Delfino", "Daniel Davila", "Pedro Urquiola", "Lionel Messi", "Luis Suarez"]
    datos = {"tecnologia": "Rengoku", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)





from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro, Pelicula, Socio
# Create your views here.


# Pagina de inicio
def index(req):
    return render(req, "index.html")

#Vista de Libros 
def libros(req):

    lista = Libro.objects.all()

    return render(req, "libros.html", {"libros": lista})

def agregar_libro(req):

    if req.method == 'POST':
        nuevo_libro = Libro(nombre=req.POST['nombre'],autor=req.POST['autor'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_libro.save()
        lista = Libro.objects.all()
        return render(req, "libros.html", {"libros": lista})
    else:
        return render(req, "agregar_libro.html", {})
    
def buscar_libro(req):
        
    return render(req, "buscar_libro.html")
    
def buscar(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        libros = Libro.objects.filter(nombre=nombre)
        return render(req, "buscar_libro.html", {"libros": libros})

    else:
        return render(req, "buscar_libro.html", {"message":"No se encontro ningun libro con ese nombre"})

# Vista de peliculas
def peliculas(req):
    lista = Pelicula.objects.all()
    return render(req, "peliculas.html", {"peliculas": lista})


def agregar_pelicula(req):

    if req.method == 'POST':
        nuevo_pelicula = Pelicula(nombre=req.POST['nombre'],director=req.POST['director'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_pelicula.save()
        lista = Pelicula.objects.all()
        return render(req, "peliculas.html", {"peliculas": lista})
    else:
        return render(req, "agregar_pelicula.html", {})

def buscar_pelicula_form(req):
        
    return render(req, "buscar_peliculas.html")

def buscar_pelicula(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        peliculas = Pelicula.objects.filter(nombre=nombre)
        return render(req, "buscar_peliculas.html", {"peliculas": peliculas})

    else:
        return render(req, "buscar_peliculas.html", {"message":"No se encontro ningun libro con ese nombre"})
    
#Socios
def socios(req):
    lista = Socio.objects.all()
    return render(req, "socios.html", {"lista_socios": lista})

def agregar_socio(req):

    if req.method == 'POST':
        nuevo_socio = Socio(nombre=req.POST['nombre'],numero_carnet=req.POST['numero_carnet'])
        nuevo_socio.save()
        lista = Socio.objects.all()
        return render(req, "socios.html", {"socios":lista})
    else:
        return render(req, "agregar_socio.html", {})
    
def buscar_socio_form(req):
        
    return render(req, "buscar_socios.html")

def buscar_socio(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        socios = Socio.objects.filter(nombre=nombre)
        return render(req, "buscar_socios.html", {"socios": socios})

    else:
        return render(req, "buscar_socios.html", {"message":"No se encontro ningun libro con ese nombre"})




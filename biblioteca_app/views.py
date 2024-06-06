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


# Vista de peliculas
def peliculas(req):
    lista = Pelicula.objects.all()
    return render(req, "peliculas.html", {"lista_peliculas": lista})


def agregar_pelicula(req):

    if req.method == 'POST':
        nuevo_pelicula = Pelicula(nombre=req.POST['nombre'],director=req.POST['director'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_pelicula.save()
        lista = Pelicula.objects.all()
        return render(req, "peliculas.html", {"peliculas": lista})
    else:
        return render(req, "agregar_pelicula.html", {})

#Socios
def socios(req):
    return render(req, "socios.html", {})

def lista_socios(req):

    lista = Socio.objects.all()

    return render(req, "socios.html", {"lista_socios": lista})

def agregar_socio(req):

    if req.method == 'POST':
        nuevo_socio = Pelicula(nombre=req.POST['nombre'],autor=req.POST['autor'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_socio.save()
        return render(req, "socios.html", {})
    else:
        return render(req, "socios.html", {})






from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro, Pelicula, Socio
# Create your views here.


# Pagina de inicio
def index(req):
    return render(req, "index.html")

#Vista de Libros 
def libros(req):
    return render(req, "libros.html")

def lista_libros(req):

    lista = Libro.objects.all()

    return render(req, "libros.html", {"lista_libros": lista})

def agregar_libro(req):

    if req.method == 'POST':
        nuevo_libro = Libro(nombre=req.POST['nombre'],autor=req.POST['autor'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_libro.save()
        return render(req, "libros.html", {})
    else:
        return render(req, "libros.html", {})


# Vista de peliculas
def peliculas(req):
    return render(req, "peliculas.html", {})

def lista_peliculas(req):

    lista = Pelicula.objects.all()

    return render(req, "peliculas.html", {"lista_peliculas": lista})

def agregar_pelicula(req):

    if req.method == 'POST':
        nuevo_pelicula = Libro(nombre=req.POST['nombre'],autor=req.POST['director'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_pelicula.save()
        return render(req, "peliculas.html", {})
    else:
        return render(req, "peliculas.html", {})

#Socios
def socios(req):
    return render(req, "socios.html", {})

def lista_socios(req):

    lista = Socio.objects.all()

    return render(req, "socios.html", {"lista_socios": lista})

def agregar_socio(req):

    if req.method == 'POST':
        nuevo_socio = Libro(nombre=req.POST['nombre'],autor=req.POST['autor'],genero=req.POST['genero'], anio_publicacion=req.POST['anio'], stock=req.POST['stock'])
        nuevo_socio.save()
        return render(req, "socios.html", {})
    else:
        return render(req, "socios.html", {})






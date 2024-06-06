from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro, Pelicula, Socio
# Create your views here.


# Pagina de inicio
def index(req):
    return render(req, "index.html")

#Vista de Libros 
def libros(req):
    return render(req, "libros.html", {})

def lista_libros(req):

    lista = Libro.objects.all()

    return render(req, "libros.html", {"lista_libros": lista})
# Vista de peliculas
def peliculas(req):
    return render(req, "peliculas.html", {})

def lista_peliculas(req):

    lista = Pelicula.objects.all()

    return render(req, "peliculas.html", {"lista_peliculas": lista})

#Socios
def socios(req):
    return render(req, "socios.html", {})

def lista_socios(req):

    lista = Socio.objects.all()

    return render(req, "socios.html", {"lista_socios": lista})

def agregar_libro(req):

    nuevo_libro = Libro(nombre="Python Basico",autor="Ivan Krysiuk",genero="Programacion", anio_publicacion="2024")
    nuevo_libro.save()
    return HttpResponse(f"""
        <p>Libro: {nuevo_libro.nombre} de {nuevo_libro.autor} añadido correctamente.</p>
    """)





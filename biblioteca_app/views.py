from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro
# Create your views here.

def agregar_libro(req):

    nuevo_libro = Libro(nombre="Python Basico",autor="Ivan Krysiuk",genero="Programacion", anio_publicacion="2024")
    nuevo_libro.save()
    return HttpResponse(f"""
        <p>Libro: {nuevo_libro.nombre} de {nuevo_libro.autor} añadido correctamente.</p>
    """)

def lista_libros(req):

    lista = Libro.objects.all()

    return render(req, "lista_libros.html", {"lista_libros": lista})
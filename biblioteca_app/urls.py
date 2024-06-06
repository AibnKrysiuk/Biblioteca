from django.contrib import admin
from django.urls import path
from .views import index, libros, agregar_libro, peliculas,agregar_pelicula, socios 


urlpatterns = [
    path('', index, name='inicio'),
    path('libros/', libros, name='libros'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('peliculas/', peliculas, name='peliculas'),
    path('agregar_pelicula/', agregar_pelicula, name='agregar_pelicula'),
    path('socios/', socios, name='socios'),
]
from django.contrib import admin
from django.urls import path
from .views import index, libros, agregar_libro,buscar_libro,buscar, peliculas,agregar_pelicula,buscar_pelicula_form,buscar_pelicula, socios, agregar_socio, buscar_socio_form,buscar_socio


urlpatterns = [
    path('', index, name='inicio'),
    path('libros/', libros, name='libros'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('buscar_libro/', buscar_libro, name='buscar_libro'),
    path('buscar/', buscar, name='buscar'),

    path('peliculas/', peliculas, name='peliculas'),
    path('agregar_pelicula/', agregar_pelicula, name='agregar_pelicula'),
    path('buscar_pelicula/', buscar_pelicula, name='buscar_pelicula'),
    path('buscar_pelicula_form/', buscar_pelicula_form, name='buscar_pelicula_form'),

    path('socios/', socios, name='socios'),
    path('agregar_socio/', agregar_socio, name='agregar_socio'),
    path('buscar_socio_form/', buscar_socio_form, name='buscar_socio_form'),
    path('buscar_socio/', buscar_socio, name='buscar_socio'),
]
from django.contrib import admin
from django.urls import path
from .views import index, lista_libros, lista_peliculas, socios 


urlpatterns = [
    path('', index, name='inicio'),
    path('libros/', lista_libros, name='libros'),
    path('peliculas/', lista_peliculas, name='peliculas'),
    path('socios/', socios, name='socios'),
]
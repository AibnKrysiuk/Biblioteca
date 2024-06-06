from django.contrib import admin
from django.urls import path
from .views import index, libros, peliculas, socios 


urlpatterns = [
    path('', index),
    path('libros', libros),
    path('peliculas/', peliculas),
    path('socios/', socios),
]
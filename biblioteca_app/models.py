from django.db import models

# Create your models here.


class Libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    anio_publicacion = models.IntegerField()
    stock = models.IntegerField()

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    anio_publicacion = models.IntegerField()
    stock = models.IntegerField()

class Socio(models.Model):
    nombre = models.CharField(max_length=40)
    numero_carnet = models.IntegerField()
    libros = models.ManyToManyField(Libro)
    peliculas = models.ManyToManyField(Pelicula)
    

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    celular = models.IntegerField()
    direccion = models.CharField(max_length=40)
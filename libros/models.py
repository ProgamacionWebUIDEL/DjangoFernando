from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100, help_text='title of messages')
    autor = models.CharField(max_length=100, help_text='autor of messages')
    numero_paginas = models.IntegerField(help_text='numero de paginas del texto')
    anio_publicacion = models.DateField(help_text='anio de publicacion', null=True )
    isbn = models.CharField(max_length=100, help_text='ISBN del libro', null=True)

class Auto(models.Model):
    marca = models.CharField(max_length=100, help_text='marca del vehiculo')
    modelo = models.CharField(max_length=100, help_text='modelo del vehiculo')
    cilindraje = models.FloatField(help_text='ingresa el cilindraje')


class Computadora(models.Model):
    marca = models.CharField(max_length=100, help_text='marca de la computadora')
    modelo = models.CharField(max_length=100, help_text='modelo del computador')
    ram = models.CharField(max_length=10, help_text='capacidad de la memoria ram')
    almacenamiento = models.CharField(max_length=15, help_text='almacenamiento')
    procesador = models.CharField(max_length=100, help_text='procesador')
    pantalla = models.CharField(max_length=100, help_text='dimension de la pantalla')
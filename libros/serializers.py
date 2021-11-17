from django.db.models import fields
from rest_framework import serializers
from .models import Libro, Auto, Computadora


class LibroSerializable(serializers.ModelSerializer):
    class Meta:

        model = Libro
        fields = (
            'titulo', 
            'autor',
            'numero_paginas'
        )

class AutoSerializable(serializers.ModelSerializer):
    class Meta:

        model = Auto
        fields = (

            'marca',
            'modelo',
            'cilindraje'
        )

class ComputadoraSerializable(serializers.ModelSerializer):
    class Meta:

        model = Auto
        fields = (

            'marca',
            'modelo',
            'ram',
            'almacenamiento',
            'procesador',
            'pantalla',
            'color'
        )
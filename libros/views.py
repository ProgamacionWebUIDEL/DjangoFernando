from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializable, AutoSerializable, ComputadoraSerializable
from .models import Libro, Auto, Computadora

# Create your views here.
class LibroVista(viewsets.ModelViewSet):
    serializer_class: LibroSerializable
    queryset = Libro.objects.all()

class AutoVista(viewsets.ModelViewSet):
    serializer_class: AutoSerializable
    queryset = Auto.objects.all()

class ComputadoraVista(viewsets.ModelViewSet):
    serializer_class: ComputadoraSerializable
    queryset = Computadora.objects.all()


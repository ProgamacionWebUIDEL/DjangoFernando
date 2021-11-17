from django.contrib import admin
from .models import Libro, Auto, Computadora
# Register your models here.
admin.site.register(Libro)
admin.site.register(Auto)
admin.site.register(Computadora)
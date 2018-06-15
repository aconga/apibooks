from django.contrib import admin
from . import models


@admin.register(models.Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    readonly_fields = ['slug']


@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    readonly_fields = ['slug']

from django.conf import settings
from django.db import models
from django.urls import reverse
from apibooks.core.models import SlugModel
from . import utils
from rest_framework.reverse import reverse as api_reverse


class Genero(SlugModel):
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Libro(SlugModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vendido = models.BooleanField(default=False)
    editorial = models.CharField(max_length=120, blank=True, null=True)
    generos = models.ManyToManyField(Genero, blank=True)
    portada = models.ImageField('Portada', upload_to=utils.ruta_de_portadas, blank=True)
    resumen = models.TextField(blank=True)
    paginas = models.IntegerField(blank=True, null=True)
    fecha_de_publicacion = models.DateField(blank=True, null=True)  # fecha de publicación para cálculos
    edicion = models.IntegerField(blank=True, null=True)
    idioma = models.CharField(max_length=120, blank=True, null=True)
    doc = models.FileField(upload_to='Doc/', blank=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse("api-libros:libro-crud", kwargs={'slug': self.slug}, request=request)

Libro._meta.get_field('nombre').verbose_name = 'Título'

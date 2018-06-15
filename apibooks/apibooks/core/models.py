from django.db import models
from uuslug import uuslug
from .utils import format_datetime


class CreateModel(models.Model):
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        abstract = True

    def str_create_date(self):
        return format_datetime(self.created)


class EditedModel(models.Model):
    edited = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        abstract = True

    def str_edited_date(self):
        return format_datetime(self.edited)


class SlugModel(models.Model):
    nombre = models.CharField('Nombre', max_length=180, db_index=True)
    slug = models.SlugField('slug', max_length=96, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.nombre, instance=self)
        super(SlugModel, self).save(*args, **kwargs)

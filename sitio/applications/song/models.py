from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import os
import time

def upload_to(instance, filename):
    # Obtener el nombre de la clase del modelo
    model_name = instance.__class__.__name__.lower()  # "artist", "album", "song"
    # Crear un nuevo nombre con timestamp
    new_filename = f"{int(time.time())}_{filename}"
    # Retornar la nueva ruta en la carpeta correspondiente
    return os.path.join(f'img/{model_name}/', new_filename)

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre artistico")
    real_name = models.CharField(max_length=100, verbose_name="Nombre real")
    nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=upload_to)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name="Fecha de lanzamiento")
    portada = models.ImageField(upload_to=upload_to)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    name_spanish = models.CharField(max_length=50, verbose_name="Nombre español", null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    lyrics_original = CKEditor5Field(verbose_name="Letra original", config_name='extends')
    lyrics_spanish = CKEditor5Field(verbose_name="Letra español", config_name='extends', null=True, blank=True)
    artists = models.ManyToManyField(Artist, verbose_name="Artistas")
    video = models.CharField(max_length=100)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self):
        return self.name

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import os
import time
import base64
from io import BytesIO
from PIL import Image

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
    imagen = models.ImageField(upload_to=upload_to, blank=True, null=True)
    imagen_base64 = models.TextField(blank=True, null=True)  # Para almacenar imagen en base64
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self):
        return self.name

    def convert_image_to_base64(self, image_field):
        """Convierte una imagen cargada a Base64"""
        # Abrir la imagen con Pillow
        image = Image.open(image_field)
        image_format = image.format.lower()
        # Guardar la imagen en un buffer
        buffered = BytesIO()
        image.save(buffered, format=image_format)  # O el formato que corresponda
        # Convertir el buffer a Base64
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return f"data:image/{image_format};base64,{img_str}"
    
    def save(self, *args, **kwargs):
        # Si hay una imagen, convertirla a Base64
        if self.imagen:
            self.imagen_base64 = self.convert_image_to_base64(self.imagen)
        super().save(*args, **kwargs)

class Album(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name="Fecha de lanzamiento")
    portada = models.ImageField(upload_to=upload_to)
    portada_base64 = models.TextField(blank=True, null=True)  # Para almacenar imagen en base64
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def convert_image_to_base64(self, image_field):
        """Convierte una imagen cargada a Base64"""
        # Abrir la imagen con Pillow
        image = Image.open(image_field)
        image_format = image.format.lower()
        # Guardar la imagen en un buffer
        buffered = BytesIO()
        image.save(buffered, format=image_format)  # O el formato que corresponda
        # Convertir el buffer a Base64
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return f"data:image/{image_format};base64,{img_str}"

    def save(self, *args, **kwargs):
        # Si hay una imagen, convertirla a Base64
        if self.portada:
            self.portada_base64 = self.convert_image_to_base64(self.portada)
        super().save(*args, **kwargs)

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

from django.contrib import admin
from .models import Artist, Song, Album

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'real_name', 'nacimiento', 'ciudad', 'pais')
    search_fields = ('name', 'real_name')
    fields = ('name', 'real_name', 'nacimiento', 'ciudad', 'pais', 'imagen', 'imagen_base64')

    def save_model(self, request, obj, form, change):
        """Guardar la imagen en base64 automáticamente al cargar una imagen"""
        if obj.imagen:
            obj.imagen_base64 = obj.convert_image_to_base64(obj.imagen)
        super().save_model(request, obj, form, change)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song)
admin.site.register(Album)

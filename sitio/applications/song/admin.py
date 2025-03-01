from django.contrib import admin
from django.utils.html import format_html
from .models import Artist, Song, Album

class AlbumFilter(admin.SimpleListFilter):
    title = "Álbum"  # Nombre que aparecerá en la barra lateral
    parameter_name = "album"  # Nombre del parámetro en la URL

    def lookups(self, request, model_admin):
        """Retorna una lista de álbumes disponibles para filtrar."""
        albums = Album.objects.all().values_list("id", "name")
        return [(album[0], album[1]) for album in albums]

    def queryset(self, request, queryset):
        """Filtra las canciones según el álbum seleccionado."""
        if self.value():
            return queryset.filter(album_id=self.value())
        return queryset

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'real_name', 'nacimiento', 'ciudad', 'pais')
    search_fields = ('name', 'real_name')
    fields = ('name', 'real_name', 'nacimiento', 'ciudad', 'pais', 'imagen', 'image_preview')
    readonly_fields = ('created', 'updated', 'image_preview')

    def image_preview(self, obj):
        if obj.imagen_base64:
            return format_html(f'<img src="{obj.imagen_base64}" width="150" />')
        return "No image"
    image_preview.short_description = "Imagen actual"

    def save_model(self, request, obj, form, change):
        """Guardar la imagen en base64 automáticamente al cargar una imagen"""
        if obj.imagen:
            obj.imagen_base64 = obj.convert_image_to_base64(obj.imagen)
        super().save_model(request, obj, form, change)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release_date', 'portada')
    search_fields = ('name', 'artist__name')
    fields = ('name', 'artist', 'release_date', 'portada', 'image_preview')
    readonly_fields = ('created', 'updated', 'image_preview')

    def image_preview(self, obj):
        if obj.portada_base64:
            return format_html(f'<img src="{obj.portada_base64}" width="150" />')
        return "No image"
    image_preview.short_description = "Imagen actual"

    def save_model(self, request, obj, form, change):
        """Guardar la imagen en base64 automáticamente al cargar una imagen"""
        if obj.portada:
            obj.portada_base64 = obj.convert_image_to_base64(obj.portada)
        super().save_model(request, obj, form, change)

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'get_artist_name')
    search_fields = ('name', 'album__name', 'album__artist__name')
    # fields = ('name', 'name_spanish', 'album', 'lyrics_original', 'lyrics_spanish', 'artists', 'video')
    readonly_fields = ('created', 'updated')
    list_filter = ('artists', AlbumFilter)

    fieldsets = (
        ("Información General", {
            "fields": ("name", "name_spanish", "album", "artists", "video"),
        }),
        ("Letras", {
            "fields": (("lyrics_original", "lyrics_spanish"),),  # Campos en la misma línea
        }),
    )

    def get_artist_name(self, obj):
        return obj.album.artist.name
    get_artist_name.short_description = "Artista"

# Registro en administración
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

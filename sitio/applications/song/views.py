from django.shortcuts import render
from django.db import models
from .models import Artist, Album, Song
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import date

# Create your views here.
class IndexView(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "index.html"

    def get_queryset(self):
        return Artist.objects.order_by("-created")[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.order_by("-created")[:10]
        context["songs"] = Song.objects.order_by("-created")[:10]
        return context

class ArtistDetail(DetailView):
    model = Artist
    context_object_name = "artist"
    template_name = "artist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        artist = self.get_object()
        # Calcular la edad
        today = date.today()
        age = today.year - artist.nacimiento.year - ((today.month, today.day) < (artist.nacimiento.month, artist.nacimiento.day))

        context["age"] = age
        context["albums"] = Album.objects.filter(artist=artist)
        # Obtener los álbumes en los que el artista ha colaborado a través de canciones
        context["collaborated_albums"] = Album.objects.filter(song__artists=artist).exclude(artist=artist).distinct()
        context["total_albums"] = Album.objects.filter(song__artists=artist).distinct().count()
        context["total_songs"] = Song.objects.filter(artists=artist).distinct().count()
        return context

class AlbumDetail(DetailView):
    model = Album
    context_object_name = "album"
    template_name = "album.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        # context["songs"] = Song.objects.filter(album=album).order_by("track_number")
        # Ordenar primero por track_number si no es NULL, y si es NULL, ordenar por nombre
        context["songs"] = Song.objects.filter(album=album).order_by(
            models.Case(
                models.When(track_number__isnull=True, then=models.Value(1)),
                default=models.Value(0),
                output_field=models.IntegerField(),
            ),
            "track_number",
            "name",
        )
        # Obtener todos los artistas que han participado en alguna canción del álbum
        context["artists"] = Artist.objects.filter(song__album=album).exclude(id=album.artist.id).distinct()
        return context

class SongDetail(DetailView):
    model = Song
    context_object_name = "song"
    template_name = "song.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.get_object()

        # Dividimos las letras en líneas numeradas
        context["lyrics_original"] = list(enumerate(song.lyrics_original.split("\n"), start=1))
        context["lyrics_spanish"] = list(enumerate(song.lyrics_spanish.split("\n"), start=1))

        return context


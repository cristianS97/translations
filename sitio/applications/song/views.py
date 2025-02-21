from django.shortcuts import render
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
        return context

class AlbumDetail(DetailView):
    model = Album
    context_object_name = "album"
    template_name = "album.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        context["songs"] = Song.objects.filter(album=album)
        return context

from django.shortcuts import render
from .models import Artist, Album, Song
from django.views.generic.list import ListView

# Create your views here.
class IndexView(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        context["songs"] = Song.objects.all()
        return context

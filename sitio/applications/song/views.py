from django.shortcuts import render
from .models import Artist, Album, Song
from django.views.generic.list import ListView

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

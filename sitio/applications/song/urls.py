from django.urls import path
from .views import IndexView, ArtistDetail, AlbumDetail, SongDetail

urlpatterns = [
    path("", IndexView.as_view(), name="inicio"),
    path("artist/<int:pk>", ArtistDetail.as_view(), name="detalleArtista"),
    path("album/<int:pk>", AlbumDetail.as_view(), name="detalleAlbum"),
    path("song/<int:pk>", SongDetail.as_view(), name="detalleSong")
]

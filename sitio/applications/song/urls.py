from django.urls import path
from .views import IndexView, ArtistDetail

urlpatterns = [
    path("", IndexView.as_view(), name="inicio"),
    path("artist/<int:pk>", ArtistDetail.as_view(), name="detalleArtista")
]

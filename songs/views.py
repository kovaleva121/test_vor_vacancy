from rest_framework import viewsets
from .models import Artist, Album, Song, Track
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    SongSerializer,
    TrackSerializer,
    AlbumDetailSerializer
)


class ArtistViewSet(viewsets.ModelViewSet):
    """Контроллер для артиста"""
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """Контроллер для альбома"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_serializer_class(self):
        """Переопределение сериализатора при вызове детальной информации"""
        if self.action == "retrieve":
            return AlbumDetailSerializer
        return AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    """Контроллер для песни"""
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """Контроллер для трека"""
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

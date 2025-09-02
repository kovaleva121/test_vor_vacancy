from rest_framework import serializers
from songs.models import Artist, Album, Song, Track


class ArtistSerializer(serializers.ModelSerializer):
    """Сериализатор для модели артиста"""

    class Meta:
        """Метаданные"""
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для модели альбома"""
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist',
        write_only=True
    )

    class Meta:
        """Метаданные"""
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор для модели песни"""

    class Meta:
        """Метаданные"""
        model = Song
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели трека"""
    song = SongSerializer(read_only=True)
    song_id = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(),
        source='song',
        write_only=True
    )
    album = AlbumSerializer(read_only=True)
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(),
        source='almum',
        write_only=True
    )

    class Meta:
        """Метаданные"""
        model = Track
        fields = '__all__'


class AlbumDetailSerializer(AlbumSerializer):
    """Сериализатор для детального отображения альбома"""
    tracks = TrackSerializer(
        many=True,
        read_only=True,
        source="track_set"
    )

    class Meta(AlbumSerializer.Meta):
        """Метаданные"""
        fields = ["id", "title", "artist", "release_year", "tracks"]

from django.contrib import admin

from songs.models import Artist, Album, Song, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Админ - панель для артиста"""
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Админ - панель для альбома"""
    list_display = ('id', 'title', 'artist')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Админ - панель для песни"""
    list_display = ('id', 'title')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """Админ - панель для трека"""
    list_display = ('id', 'song', 'album', 'track_number')

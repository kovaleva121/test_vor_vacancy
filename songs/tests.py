from rest_framework import status
from rest_framework.test import APITestCase

from songs.models import Artist, Album, Song, Track


class BaseAPITestCase(APITestCase):
    """Тесты по CRUD операциям основных моделей"""

    def setUp(self):
        # создаем артиста, альбом, песни, трек
        self.artist = Artist.objects.create(first_name='test first name', last_name='test last_name')
        self.album = Album.objects.create(title='test title', artist=self.artist, release_year=2025)
        self.song = Song.objects.create(title='test title')
        self.song_2 = Song.objects.create(title='test 2 title')
        self.track = Track.objects.create(song=self.song, album=self.album, track_number=1)


class ArtistViewSetTests(BaseAPITestCase):
    """Тесты для ArtistViewSet"""

    def test_list_artists(self):
        """Получение списка исполнителей"""
        url = '/api/artists/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['first_name'], 'test first name')

    def test_create_artist(self):
        """Создание исполнителя"""
        url = '/api/artists/'
        data = {'first_name': 'New first name', 'last_name': 'New last name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 2)

    def test_retrieve_artist(self):
        """Получение исполнителя по ID"""
        url = f'/api/artists/{self.artist.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'test first name')

    def test_update_artist(self):
        """Обновление исполнителя"""
        url = f'/api/artists/{self.artist.pk}/'
        data = {'first_name': 'Updated first name'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.first_name, 'Updated first name')

    def test_delete_artist(self):
        """Удаление исполнителя"""
        url = f'/api/artists/{self.artist.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 0)


class AlbumViewSetsTests(BaseAPITestCase):
    """Тесты для AlbumViewSet"""

    def test_list_album(self):
        """Получение списка альбомов"""
        url = '/api/albums/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'test title')

    def test_create_album(self):
        """Создания альбома"""
        url = '/api/albums/'
        data = {
            'title': 'new title',
            'artist_id': self.artist.id,
            'release_year': 2024
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 2)

    def test_retrieve_album(self):
        """Получение альбома по ID"""
        url = f'/api/albums/{self.album.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test title')

    def test_update_album(self):
        """Обновление альбома"""
        url = f'/api/albums/{self.album.pk}/'
        data = {'title': 'update title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'update title')

    def test_delete_album(self):
        """Удаление альбома"""
        url = f'/api/albums/{self.album.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 0)


class SongViewSetsTests(BaseAPITestCase):
    """Тесты для SongViewSet"""

    def test_list_song(self):
        """Получения списка песен"""
        url = '/api/songs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'test title')

    def test_create_song(self):
        """Создание песни"""
        url = '/api/songs/'
        data = {'title': 'new title'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 3)

    def test_retrieve_song(self):
        """Получение песни по ID"""
        url = f'/api/songs/{self.song.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test title')

    def test_update_song(self):
        """Обновление песни"""
        url = f'/api/songs/{self.song.pk}/'
        data = {'title': 'update title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'update title')

    def test_delete_song(self):
        """Удаление песни"""
        url = f'/api/songs/{self.song.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), 1)


class TrackViewSetsTests(BaseAPITestCase):
    """Тесты для TrackViewSet"""

    def test_list_track(self):
        """Получение списка треков"""
        url = '/api/tracks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['track_number'], 1)

    def test_create_track(self):
        """Создание трека"""
        url = '/api/tracks/'
        data = {'song_id': self.song_2.id,
                'album_id': self.album.id,
                'track_number': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Track.objects.count(), 2)

    def test_retrieve_track(self):
        """Получение трека по ID"""
        url = f'/api/tracks/{self.track.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['track_number'], 1)

    def test_update_track(self):
        """Обновление трека"""
        url = f'/api/tracks/{self.track.pk}/'
        data = {'track_number': 3}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['track_number'], 3)

    def test_delete_track(self):
        """Удаление трека"""
        url = f'/api/tracks/{self.track.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Track.objects.count(), 0)

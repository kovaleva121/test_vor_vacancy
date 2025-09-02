from django.db import models


class Artist(models.Model):
    """Модель - исполнитель"""
    first_name = models.CharField(max_length=100, verbose_name='Имя', help_text='Укажите имя исполнителя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', help_text='Укажите фамилию исполнителя')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        """Строковое отображение"""
        return f'{self.first_name} {self.last_name}'


class Album(models.Model):
    """Модель - альбом"""
    title = models.CharField(max_length=255, verbose_name='Название альбома', help_text='Напишите название альбома')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель', related_name='albums',
                               help_text='Укажите исполнителя альбома')
    release_year = models.PositiveIntegerField(verbose_name='Год выпуска', help_text='Укажите год выпуска')

    class Meta:
        """Метаданные"""
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        """Строковое отображение"""
        return f'{self.performer}, {self.release_year}'


class Song(models.Model):
    """Модель - песни"""
    title = models.CharField(max_length=250, verbose_name='Название песни', help_text='Укажите название песни')
    albums = models.ManyToManyField(Album, through='Track', related_name='songs', verbose_name='Альбомы',
                                    help_text='Укажите альбомы')

    class Meta:
        """Метаданные"""
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        """Строковое отображение"""
        return self.title


class Track(models.Model):
    """Модель - трек"""
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Песня')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')
    track_number = models.PositiveIntegerField(verbose_name='Порядковый номер в альбоме',
                                               help_text='Укажите порядковый номер')

    class Meta:
        """Метаданные"""
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
        unique_together = [["album", "track_number"], ["album", "song"]]

    def __str__(self):
        """Строковое отображение"""
        return f"{self.track_number}. {self.song.title} - {self.album.title}"

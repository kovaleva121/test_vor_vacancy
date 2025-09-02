from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from .apps import SongsConfig
from .views import ArtistViewSet, AlbumViewSet, SongViewSet, TrackViewSet

app_name = SongsConfig.name

router = DefaultRouter()
router.register(r"artists", ArtistViewSet, basename='artist')
router.register(r"albums", AlbumViewSet, basename='album')
router.register(r"songs", SongViewSet, basename='song')
router.register(r"tracks", TrackViewSet, basename='track')

urlpatterns = [path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
               path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
               path('api/', include(router.urls)),
               ]

from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from .apps import SongsConfig
from .views import ArtistViewSet, AlbumViewSet, SongViewSet, TrackViewSet

app_name = SongsConfig.name

router = DefaultRouter()
router.register(r"artists", ArtistViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"songs", SongViewSet)
router.register(r"tracks", TrackViewSet)

urlpatterns = [path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
               path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), ]

urlpatterns += router.urls

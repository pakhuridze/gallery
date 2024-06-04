from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtworkViewSet, ExhibitionsViewSet

router = DefaultRouter()
router.register(r"artists", ArtistViewSet)
router.register(r"artworks", ArtworkViewSet)
router.register(r"exhibitions", ExhibitionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

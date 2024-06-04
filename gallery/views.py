from .models import Artist, ArtWork, Exhibition
from rest_framework import viewsets
from .serializers import ArtistSerializer, ArtWorkSerializer, ExhibitionSerializer
from .permissions import isAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ArtWorkFilter


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [isAdminOrReadOnly, IsAuthenticated]


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = ArtWork.objects.all()
    serializer_class = ArtWorkSerializer
    permission_classes = [isAdminOrReadOnly, IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["artist", "creation_date"]
    filterset_class = ArtWorkFilter


class ExhibitionsViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [isAdminOrReadOnly, IsAuthenticated]


# add comm

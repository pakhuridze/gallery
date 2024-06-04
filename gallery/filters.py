import django_filters
from .models import ArtWork


class ArtWorkFilter(django_filters.FilterSet):
    class Meta:
        model = ArtWork
        fields = ["artist", "creation_date"]

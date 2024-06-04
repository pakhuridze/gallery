from rest_framework import serializers
from .models import Artist, ArtWork, Exhibition


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields = "__all__"


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = "__all__"

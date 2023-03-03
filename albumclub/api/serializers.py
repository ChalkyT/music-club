from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    #Meta data class describing the model
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'artwork']

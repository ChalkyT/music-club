# Serialization with enable us to turn Python objects into Json format

from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta: # Inner class containing Meta Data describing the model
        model = Album # model is an Album imported from .models
        fields = ['id', 'title', 'artist', 'artwork'] # This is a list and id is included because it is automatically added to the model

        #Using the serializer when we are returning our model through the API
        #Need to create end points in views.py 

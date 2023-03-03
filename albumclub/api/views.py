from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Album
from .serializers import AlbumSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework import authentication, permissions
# from rest_framework.renderers import JSONRenderer

# class GreetingApi(APIView):
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         return Response({'message': 'Hello world'})

# class AlbumsApi(APIView):
#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         response = self.album_list(request)
#         return Response(response)

@api_view(['GET', 'POST'])
def all_albums(request, format=None):

    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response({'albums':serializer.data})

    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, id, format=None):

    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response({'albums':serializer.data})
    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'albums':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

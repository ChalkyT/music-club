from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#The CRUD methods added here allow you to access the API directly using http requests. 
#Responses to requests can be returned as html or Json.
#Without this view.py file you could only add album information via the admin pages using the models. 

@api_view(['GET', 'POST']) #function based view decorator
#This view accepts the GET and POST methods and they are passed in as one argument in a list
def all_albums(request, format=None): #format is defaulted to None so that we can use format_suffix_patterns in views.py to view api/albums.json
    
    if request.method == 'GET': #Gets all the albums
        albums = Album.objects.all() # assign all the albums (that are objects) to a variable called albums
        serializer = AlbumSerializer(albums, many=True) #Takes all the albums and serializes them (turns them into binary format) (many=True will serialize all of the albums), then assign to variable called serializer 
        return Response({'albums':serializer.data}) #returns the serialized data with the option of Json or html output 
        #To return as a dictionary I've added  {'albums':serializer.data} instead of just (serializer.data)
    
    if request.method == 'POST':
        #takes the data given, deserializes it and then creates an object 
        serializer = AlbumSerializer(data=request.data) #data inputted via request
        if serializer.is_valid(): #check if data is valid
            serializer.save() #save data if valid
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
            #Django does a lot of behind the scenes work here so we only have to pass in the serialized data and the status

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, id, format=None): #Here we are using this function to access ../api/albums/1 for example

    try: #to check if the id being passed in is a valid request
        album = Album.objects.get(pk=id) #passing in the primary key. If it is valid then assign to a variable called album to be used in this function
    except Album.DoesNotExist: #throws an exception
        return Response(status=status.HTTP_404_NOT_FOUND) #use this http status from the list of options

    if request.method == 'GET':
        serializer = AlbumSerializer(album) #puts serialized data into a variable called serializer
        return Response({'albums':serializer.data}) #returns the serialized data in Json in the form of a dictionary called 'albums'

    elif request.method == 'PUT': #elif so only one of the options will be executed at a time
        serializer = AlbumSerializer(album, data=request.data) #Need to pass in data being sent with request 
        if serializer.is_valid(): #check it is valid data 
            serializer.save() 
            return Response({'albums':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #if not valid data 

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#ignore all this for now - leaving in to explore using classes and APIview instead of @api_view with functions

# from rest_framework import authentication, permissions
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView

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
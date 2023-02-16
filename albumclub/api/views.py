from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.renderers import JSONRenderer

# Create your views here.
class GreetingApi(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        return Response({'message': 'Hello world'})

class AlbumsApi(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        return Response({'album': 'Rumours'})
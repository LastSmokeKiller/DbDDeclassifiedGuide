from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class DbdApiView(APIView):
    """Test API view"""
    # serializer_class = serializers.

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'This is a test case for Dbd Declassified',
            'This is the perks viewer test',
            'This is the power viewer test',
            'The cake is a lie'
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with out name"""


        
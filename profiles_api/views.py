from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers


class HelloApiView(APIView):
    """
    Test API View
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIView Features
        :param request:
        :param format:
        :return:
        """
        an_apiview = [
           'A', "B", "C", 'D'
        ]

        return Response({'message': 'Hello!',
                         'an_apiview': an_apiview})

    def post(self, request):
        """
        Create a hello message with our name
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """
        Handles updating an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handles a partial update of any object
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Deletes an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'DELETE'})
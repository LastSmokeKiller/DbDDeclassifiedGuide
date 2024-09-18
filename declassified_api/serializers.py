from rest_framework import serializers

from declassified_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=20)

class UserSerializer(serializers.ModelSerializer):
    """Serializers a user object"""

    class Meta:
        model = models.User
        fields = (
            'id',
            'email',
            'username',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
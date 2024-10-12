from .models.model_survivorperk import SurvivorPerk
from rest_framework import serializers


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

        
class SurvivorPerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurvivorPerk
        fields = ['id','name','common','survivor','dlc','licensed','description'
                  ,'use_case','best_pair','best_exp','neutral_pair','neutral_exp','bad_pair','bad_exp'
                  ,'rating','community_rating','site_rating']
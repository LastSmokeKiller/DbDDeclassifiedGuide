from rest_framework import serializers
from dbdeclassified.models import Killer

class KillerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Killer
        fields = ['id','name','common','dlc','licensed','description'
                  ,'rating','community_rating','site_rating']
        read_only_fields = fields
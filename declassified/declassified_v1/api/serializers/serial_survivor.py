from rest_framework import serializers
from declassified.models.model_survivor import Survivor

class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id','name','nickname','dlc_id','survivor_perks']
        read_only_fields = fields
from rest_framework import serializers
from dbdeclassified.models import DLC

class DLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLC
        fields = ['id','name','survivors','killers','licensed','free','dlc_buy','dollar_cost']
        read_only_fields = fields
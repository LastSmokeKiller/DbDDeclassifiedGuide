from rest_framework import serializers
from dbdeclassified.models import KillerPerk

class SerializerKillerPerk(serializers.ModelSerializer):
    class Meta:
        model = KillerPerk
        fields = ['id','name','common','killer_id','description'
                  ,'use_case','best_pair','best_exp','neutral_pair','neutral_exp','bad_pair','bad_exp'
                  ,'rating','community_rating','site_rating']
        read_only_fields = ['id','name','common','killer_id','description'
                  ,'use_case','best_pair','best_exp','neutral_pair','neutral_exp','bad_pair','bad_exp'
                  ,'rating','site_rating']
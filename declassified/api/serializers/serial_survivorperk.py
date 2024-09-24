from rest_framework import serializers
from declassified.models import SurvivorPerk

class SurvivorPerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurvivorPerk
        fields = ['id','name','common','survivor','dlc','licensed','description'
                  ,'use_case','best_pair','best_exp','neutral_pair','neutral_exp','bad_pair','bad_exp'
                  ,'rating','community_rating','site_rating']
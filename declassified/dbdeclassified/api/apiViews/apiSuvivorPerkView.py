from rest_framework import viewsets

from dbdeclassified.api.serializers.serial_survivorperk import SurvivorPerkSerializer
from dbdeclassified.models import SurvivorPerk

class SurvivorPerkViewSet(viewsets.ModelViewSet):
    queryset = SurvivorPerk.objects.all().order_by('id')
    serializer_class = SurvivorPerkSerializer


from rest_framework import viewsets

from dbdeclassified.api.serializers.serial_survivor import SurvivorSerializer
from dbdeclassified.models import Survivor

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all().order_by('id')
    serializer_class = SurvivorSerializer
from rest_framework import viewsets

from declassified.api.serializers.serial_survivor import SurvivorSerializer
from declassified.models.model_survivor import Survivor

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all().order_by('id')
    serializer_class = SurvivorSerializer
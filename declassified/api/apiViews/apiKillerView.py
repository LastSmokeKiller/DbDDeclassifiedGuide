from rest_framework import viewsets

from declassified.api.serializers.serial_killer import KillerSerializer
from declassified.models.model_killer import Killer

class KillerViewSet(viewsets.ModelViewSet):
    queryset = Killer.objects.all().order_by('id')
    serializer_class = KillerSerializer
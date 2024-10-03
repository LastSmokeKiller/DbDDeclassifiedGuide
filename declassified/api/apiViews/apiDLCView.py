from rest_framework import viewsets

from declassified.api.serializers.serial_dlc import DLCSerializer
from declassified.models.model_dlc import DLC

class DLCViewSet(viewsets.ModelViewSet):
    queryset = DLC.objects.all().order_by('id')
    serializer_class = DLCSerializer
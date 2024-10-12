from rest_framework import viewsets

from dbdeclassified.api.serializers.serial_dlc import DLCSerializer
from dbdeclassified.models import DLC

class DLCViewSet(viewsets.ModelViewSet):
    queryset = DLC.objects.all().order_by('id')
    serializer_class = DLCSerializer
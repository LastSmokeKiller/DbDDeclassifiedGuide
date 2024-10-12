from rest_framework import viewsets

from dbdeclassified.api.serializers.serial_killer import KillerSerializer
from dbdeclassified.models import Killer

class KillerViewSet(viewsets.ModelViewSet):
    queryset = Killer.objects.all().order_by('id')
    serializer_class = KillerSerializer
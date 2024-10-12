from rest_framework import viewsets

from declassified.api.serializers.serial_killerperk import SerializerKillerPerk
from declassified.models import KillerPerk

class KillerPerkViewSet(viewsets.ModelViewSet):
    queryset = KillerPerk.objects.all().order_by('id')
    serializer_class = SerializerKillerPerk
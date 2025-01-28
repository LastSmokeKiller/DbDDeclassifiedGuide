from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import get_object_or_404


from declassified.api.serializers.serial_iridescentcalc import IridescentCalcSerializer
from dbdeclassified.models import IridescentCalc


class IridescentCalcViewSet(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'iridescentcalc.html'

    serializer_class = IridescentCalcSerializer
    queryset = IridescentCalc.objects.all()
    

    def get(self, request, format=None):
        calc = get_object_or_404(IridescentCalc, pk=1)
        serializer = IridescentCalcSerializer(calc)
        return Response({'serializer': serializer, 'calc': calc})
    
    
        


from rest_framework import serializers
from declassified.models import IridescentCalc


class IridescentCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = IridescentCalc
        fields = (
            'curlvl', 
            'curiri',
            'curxp', 
            'irineeded', 
            'xpon'
        )
    
    def useCalc(self):
        IriCalc = IridescentCalc.create_iri_calc(
            curlvl = self.curlvl,
            curiri = self.curiri,
            curxp = self.curxp,
            irineeded = self.irineeded,
            xpon = self.xpon
        )
        return IriCalc

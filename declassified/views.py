from django.shortcuts import render
from django.views import View
from .models.model_iridescentcalc import IridescentCalc

class Index(View):
    def get(self, request):
        form = IridescentCalc()
        return render(request, 'IridescentCalculator/index.html',{'form': form})
    
    def post(self, request):
        pass
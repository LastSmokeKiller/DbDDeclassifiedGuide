from django.shortcuts import render
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from dbdeclassified import serializers
from dbdeclassified import models
from dbdeclassified import permissions
from .forms import IriCalcForm
from .models import IridescentCalc
#Create your views here.

class IriCalcView(View):
    def get(self, request):
        form = IriCalcForm()
        return render(request, 'IriCalc/index.html', {'form': form})

    def post(self, request):
        form  = IriCalcForm(request.POST)

        if form.is_valid():

            # Setting up calculator variables being used
            current_level = int(form.cleaned_data['current_level'])
            current_iridescent = int(form.cleaned_data['current_iridescent_shards'])
            current_xp = int(form.cleaned_data['current_xp'])
            iridescent_needed = int(form.cleaned_data['iridescent_shards_needed'])
            xpon = bool(form.cleaned_data['xpon'])
            xp_needed = 0
            level_needed = 0
            iridescent_left = 0

            # Creating calculator object and Calculating level, xp needed, and iridescent shards left over
            iricalc = IridescentCalc(current_level, current_iridescent, current_xp, iridescent_needed, xpon)
            level_needed = iricalc.CalculateLvl()
            xp_needed = iricalc.getXP()
            iridescent_left = iricalc.getIriLeft()

            # context for values being returned
            context = {
                'levels_needed': level_needed,
                'xp_needed': xp_needed,
                'iridescent_left': iridescent_left,
            }

        # render the template
        return render(request, 'IriCalc/results.html', context)
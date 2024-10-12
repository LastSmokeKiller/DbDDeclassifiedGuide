from rest_framework import routers
from dbdeclassified.api.apiViews import SurvivorPerkViewSet

router = routers.DefaultRouter()

router.register(r'Survivor/api', SurvivorPerkViewSet)
router.register(r'Survivor/api/(?P<survivor_perk_id>\d+)', SurvivorPerkViewSet)
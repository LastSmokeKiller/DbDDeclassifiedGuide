from django.urls import path, include

from rest_framework.routers import DefaultRouter

from dbdeclassified import views


router = DefaultRouter()
# router.register('dbd-viewset')


urlpatterns = [
    path('',include(router.urls))
]
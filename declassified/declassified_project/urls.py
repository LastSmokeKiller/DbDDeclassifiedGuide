from django.contrib import admin
from django.urls import path, include
from declassified.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('profiles_api.urls')),
    path('', Index)
]
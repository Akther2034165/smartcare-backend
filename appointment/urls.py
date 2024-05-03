from django.urls import path,include
from rest_framework import routers
from .views import AppointmentViewSet

routers = routers.DefaultRouter()
routers.register('', AppointmentViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

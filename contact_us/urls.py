from rest_framework.routers import DefaultRouter
from .views import ContactViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', ContactViewSet)
urlpatterns =[
    path('', include(router.urls))
]
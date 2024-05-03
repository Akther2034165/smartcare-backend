from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet,AvailableTimeViewSet, DesignationViewSet, SpecializationViewSet, ReviewViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'doctor_list', DoctorViewSet),
router.register(r'available_time', AvailableTimeViewSet),
router.register(r'designation', DesignationViewSet),
router.register(r'specialization', SpecializationViewSet),
router.register(r'reviews', ReviewViewSet),
urlpatterns =[
    path('', include(router.urls))
]
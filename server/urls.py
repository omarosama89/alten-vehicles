# from django.conf.urls import url
from .api import CustomerViewSet, VehicleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = router.urls
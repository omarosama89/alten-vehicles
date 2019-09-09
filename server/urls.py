from django.conf.urls import url
from .api import CustomerApi, VehicleApi

urlpatterns = [
    url(r'^customers$', CustomerApi.as_view()),
    url(r'^vehicles$', VehicleApi.as_view())
]
from rest_framework.generics import ListAPIView
from .serializers import CustomerSerializer, VehicleSerializer
from .models import Customer, Vehicle

class CustomerApi(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleApi(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer, VehicleSerializer
from .models import Customer, Vehicle

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    def get_queryset(self):
        status = self.request.GET.get('status')
        customer_id = self.request.GET.get('customer_id')
        if status and customer_id:
            return Vehicle.objects.filter(status=status, customer_id=customer_id)
        elif status:
            return Vehicle.objects.filter(status=status)
        elif customer_id:
            return Vehicle.objects.filter(customer_id=customer_id)
        else:
            return Vehicle.objects.all()






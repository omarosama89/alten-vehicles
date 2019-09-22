from rest_framework.generics import ListAPIView
from .serializers import CustomerSerializer, VehicleSerializer
from .models import Customer, Vehicle

class CustomerApi(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleApi(ListAPIView):
    serializer_class = VehicleSerializer
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






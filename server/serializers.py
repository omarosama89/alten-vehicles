from rest_framework import serializers
from .models import Customer, Vehicle

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'firts_name', 'last_name', 'remote_id')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'status', 'vehicle_id', 'reg_num', 'customer_id')
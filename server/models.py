from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .realtime_api import RealtimeApi



@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Vehicle(models.Model):
    status = models.CharField(max_length=20, choices=[
        ('disconnected', 'disconnected'),
        ('connected', 'connected'),
    ])
    vehicle_id = models.CharField(max_length=20)
    reg_num = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, related_name="vehicles", on_delete=models.PROTECT)
    def customer_name(self):
        return self.customer.first_name + ' ' + self.customer.last_name

@receiver(pre_save, sender=Vehicle)
def callback(sender, instance, **kwargs):
    RealtimeApi.notify('event', instance)
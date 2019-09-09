from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    remote_id = models.IntegerField()


class Vehicle(models.Model):
    status = models.CharField(max_length=20, choices=[
        ('disconnected', 'disconnected'),
        ('connected', 'connected'),
    ])
    vehicle_id = models.CharField(max_length=20)
    reg_num = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, related_name="vehicles", on_delete=models.PROTECT)

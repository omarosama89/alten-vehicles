from unittest import TestCase
from django.test import TransactionTestCase
from .models import Vehicle, Customer

class CustomerModelTestCase(TestCase):

    def test_valid_model_first_name_exists(self):
        target = Customer()
        target.first_name = 'Ahmed'
        self.assertTrue(target.first_name)

    def test_invalid_model_first_name_not_exists(self):
        target = Customer()
        self.assertFalse(target.first_name)

    def test_valid_model_last_name_exists(self):
        target = Customer()
        target.last_name = 'dafrawy'
        self.assertTrue(target.last_name)

    def test_invalid_model_last_name_not_exists(self):
        target = Customer()
        self.assertFalse(target.last_name)

class VehicleModelTestCase(TestCase):
    def test_valid_model_with_status_is_connected(self):
        target = Vehicle()
        target.status = 'connected'
        self.assertTrue(target.status)

    def test_valid_model_with_status_is_disconnected(self):
        target = Vehicle()
        target.status = 'disconnected'
        self.assertTrue(target.status)

    def test_invalid_model_with_status_is_neither(self):
        target = Vehicle()
        target.status = ''
        self.assertFalse(target.status)

    def test_invalid_model_with_status_is_empty(self):
        target = Vehicle()
        target.status = ''
        self.assertFalse(target.status)

    def test_valid_model_with_vehicle_id_exists(self):
        target = Vehicle()
        target.vehicle_id = 'YS2R4X20005399401'
        self.assertTrue(target.vehicle_id)

    def test_invalid_model_with_vehicle_id_not_exists(self):
        target = Vehicle()
        target.vehicle_id = ''
        self.assertFalse(target.vehicle_id)

    def test_valid_model_with_reg_num_exists(self):
        target = Vehicle()
        target.reg_num = 'ABC123'
        self.assertTrue(target.reg_num)

    def test_invalid_model_with_reg_num_not_exists(self):
        target = Vehicle()
        target.reg_num = ''
        self.assertFalse(target.reg_num)

class DatabaseLoaded(TransactionTestCase):
    fixtures = ['server/fixtures/unit-test.json']

    def test_fixtures_load(self):
        self.assertTrue(Customer.objects.count() > 0)

# class CustomerModelTransactionTestCase(TransactionTestCase):
#     # fixtures = ['server/fixtures/unit-test.json']
#
#     def test_first_name_persists(self):
#         new_first_name = 'kjhkjdfhkjahskj'
#         target = Customer.objects.first()
#         target.first_name = new_first_name
#         target.save()
#         self.assertEqual(target.first_name, Customer.objects.get(pk=target.pk).first_name)

from customer.api.v1.serializers import CustomerDetailSerializer, ManipulateCustomerDetailSerializer
from django.test import TestCase


class CustomerDetailSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = 'Rajprabhu'
        cls.phone_number = '+917452369841'
        cls.address = '100/100, velchery-24'
        cls.grocery = {
            'dal': '1kg',
            'vegetable': '0.5kg'
        }
        cls.landmark = 'Test'

    def test_validate_data(self):
        data = {
            'name': self.name,
            'phone_number': self.phone_number,
            'address': self.address,
            'grocery': self.grocery,
            'landmark': self.landmark
        }
        serializer = CustomerDetailSerializer(data=data)
        self.assertTrue(serializer.is_valid())


class ManipulateCustomerDetailSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = 'Rajprabhu'
        cls.phone_number = '+917452369841'
        cls.address = '100/100, velchery-24'
        cls.grocery = {
            'dal': '1kg',
            'vegetable': '0.5kg'
        }
        cls.landmark = 'Test',
        cls.order_status = 'V'

    def test_validate_data(self):
        data = {
            'name': self.name,
            'phone_number': self.phone_number,
            'address': self.address,
            'grocery': self.grocery,
            'landmark': self.landmark,
            'order_status': self.order_status
        }
        serializer = ManipulateCustomerDetailSerializer(data=data)
        self.assertTrue(serializer.is_valid())

# from django.urls import reverse
from rest_framework.test import APIClient


class CreateCustomerDetailsAPITest(APIClient):

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

from django.urls import reverse
from rest_framework.test import APIClient


class CreateCustomerDetailsAPITest(APIClient):

    @classmethod
    def setUpTestData(cls):
        cls.name = 'Rajprabhu'
        cls.phone_number = '+918754896787'
        cls.address = '74/24, velchery-24'
        cls.grocery = {
            'dal': '1kg',
            'vegetable': '0.5kg'
        }
        cls.landmark = 'Test'

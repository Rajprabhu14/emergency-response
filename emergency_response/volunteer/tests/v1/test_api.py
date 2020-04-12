# from django.urls import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from common.constants import common_failure_response, common_success_response


class CreateCustomerDetailsAPITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('volunteer:volunteer')

    def test_valid_volunteer_data(self):
        """Valid Volunteer Register"""
        data = {
            "email": "rajprabhas123a@egmore.com",
            "name": "Rajprabhu",
            "phone_number": "+918757652757",
            "address": "74/24,  velachery, chennai-42",
            "password": "Rajpabhu@123",
            "conform_password": "Rajpabhu@123",
            "is_volunteer": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_volunteer_registration.custom_code)

    def test_valid_customer_data(self):
        """Valid Volunteer Register"""
        data = {
            "email": "rajprabhas123a@egmore.com",
            "name": "Rajprabhu",
            "phone_number": "+918757652757",
            "address": "74/24,  velachery, chennai-42",
            "password": "Rajpabhu@123",
            "conform_password": "Rajpabhu@123",
            "is_customer": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_customer_registration.custom_code)

    def test_in_valid_customer_data(self):
        """Valid Volunteer Register"""
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['custom_code'],
                         common_failure_response.validation_error.custom_code)

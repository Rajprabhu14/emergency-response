from django.urls import reverse  # NOQA
from rest_framework import status
from rest_framework.test import APITestCase

from common.constants import common_failure_response, common_success_response
from common.tests import common_test_functionality


class CreateCustomerDetailsAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('customer:create_customer')
        cls.password = 'Demo@123'

    def get_data(self):
        data = {
            "name": "Rajprabhu",
            "phone_number": "+917452369841",
            "address": "100,100 , velachery, Chennai-42",
            "landmark": "School",
            "grocery": {
                'dal': '1kg',
                'vegetable': '0.5kg'
            }
        }
        return data

    def test_vaild_data(self):
        """
        Ensure we can create a new customer object.
        """
        created_user = common_test_functionality.create_data(password=self.password, is_customer=True)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        data = self.get_data()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_data_entry.custom_code)

    def test_invaild_data(self):
        """
        Ensure response Type for serializer error field
        """
        created_user = common_test_functionality.create_data(is_customer=True, password=self.password)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['custom_code'], common_failure_response.validation_error.custom_code)

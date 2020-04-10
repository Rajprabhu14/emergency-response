from django.urls import reverse  # NOQA
from rest_framework import status
from rest_framework.test import APITestCase
from common.constants import common_success_response, common_failure_response


class CreateCustomerDetailsAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # cls.name = 'Rajprabhu'
        # cls.phone_number = '+917452369841'
        # cls.address = '100,100 , velachery, Chennai-42'
        # cls.grocery = {
        #     'dal': '1kg',
        #     'vegetable': '0.5kg'
        # }
        # cls.landmark = 'Test'
        cls.url = reverse('customer:create_customer')

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
        data = self.get_data()
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_data_entry.custom_code)

    def test_invaild_data(self):
        """
        Ensure response Type for serializer error field
        """
        # data = self.get_data()
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['custom_code'], common_failure_response.validation_error.custom_code)

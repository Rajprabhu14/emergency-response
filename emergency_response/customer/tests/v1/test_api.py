from django.urls import reverse  # NOQA
from rest_framework import status
from rest_framework.test import APITestCase
from customer.models import CustomerDetails
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


class UpdateCustomerDetailsAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_url = reverse('customer:create_customer')
        cls.password = 'Demo@123'
        # cls.url = reverse('customer:customer-details')
        # print(cls.url)

    def get_data(self):
        data = {
            "name": "Rajprabhu",
            "phone_number": "+917452369841",
            "address": "100,100 , velachery, Chennai-42",
            "landmark": "School",
            "grocery": {
                'dal': '1kg',
                'vegetable': '0.5kg'
            },
            "order_status": "U"
        }
        return data

    def test_invalid_method(self):
        """
        Ensure Invalid Method response
        """
        entry_created = common_test_functionality.create_customer_grocery_entry_data()
        created_user = common_test_functionality.create_data(password=self.password, is_customer=True)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        data = self.get_data()
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['custom_code'], common_failure_response.method_not_allowed.custom_code)
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['custom_code'], common_failure_response.method_not_allowed.custom_code)

    def test_valid_get_data(self):
        """
        Ensure we can create a new customer object.
        """
        entry_created = common_test_functionality.create_customer_grocery_entry_data()
        created_user = common_test_functionality.create_data(password=self.password, is_customer=True)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        # data = self.get_data()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_retrieve.custom_code)

    def test_valid_put_data(self):
        """
        Ensure we can update of customer object.
        """
        entry_created = common_test_functionality.create_customer_grocery_entry_data()
        created_user = common_test_functionality.create_data(password=self.password, is_customer=True)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        data = self.get_data()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_update.custom_code)

    def test_valid_patch_data(self):
        """
        Ensure we can update a single value of customer object.
        """
        entry_created = common_test_functionality.create_customer_grocery_entry_data()
        created_user = common_test_functionality.create_data(password=self.password, is_customer=True)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        data = self.get_data()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_update.custom_code)

    def test_invaild_method(self):
        """
        Ensure response Type for serializer error field
        """
        created_user = common_test_functionality.create_data(is_customer=True, password=self.password)
        access_token = common_test_functionality.get_customer_access(email=created_user.email, password=self.password)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.post(self.create_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['custom_code'], common_failure_response.validation_error.custom_code)

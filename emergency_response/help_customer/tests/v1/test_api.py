# from django.urls import reverse
from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from common.constants import common_failure_response, common_success_response
from common.tests import common_test_functionality
from customer.models import CustomerDetails


class CustomerHelperListAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.resgistration_url = reverse('volunteer:volunteer')
        cls.customer_entry_url = reverse('customer:create_customer')
        cls.customer_email = 'customer@gmail.com'
        cls.volunteer_email = 'v@gmail.com'
        cls.password = 'Test@123'
        cls.url = reverse('help_customer:geo-filter-help')

    def get_customer_entry(self):
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

    def get_registration_data(self):
        data = {
            "email": '',
            "name": "Rajprabhu",
            "phone_number": "+918757652757",
            "address": "74/24,  velachery, chennai-42",
            "password": self.password,
            "conform_password": self.password,
            "is_volunteer": False,
            "is_customer": False
        }
        return data

    @mock.patch('common.utils')
    def create_customer_volunteer_data(self, mock_utils):
        """Valid Volunteer Register"""
        data = self.get_registration_data()
        data['email'] = self.volunteer_email
        data['is_volunteer'] = True
        # mock response
        mock_utils.map_my_india_api_request.return_value = {
            'longitude': 80,
            'latitude': 13
        }, True
        response = self.client.post(self.resgistration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_volunteer_registration.custom_code)

        """Valid Customer Register"""
        data = self.get_registration_data()
        data['email'] = self.customer_email
        data['is_customer'] = True
        data['phone_number'] = "+918757652756"
        response = self.client.post(self.resgistration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_customer_registration.custom_code)

    def add_customer_entry(self):
        access_token = common_test_functionality.get_customer_access(email=self.customer_email, password=self.password)
        data = self.get_customer_entry()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.post(self.customer_entry_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_data_entry.custom_code)

    def test_invalid_method(self):
        """
        Ensure Invalid Method response
        """
        self.create_customer_volunteer_data()
        self.add_customer_entry()
        access_token = common_test_functionality.get_customer_access(email=self.volunteer_email, password=self.password)
        # self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['custom_code'], common_failure_response.method_not_allowed.custom_code)

    def test_valid_data(self):
        """
        Ensure Invalid Method response
        """
        self.create_customer_volunteer_data()
        self.add_customer_entry()
        access_token = common_test_functionality.get_customer_access(email=self.volunteer_email, password=self.password)
        # self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_customer_location_volunteering.custom_code)


class MyCustomerAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.resgistration_url = reverse('volunteer:volunteer')
        cls.customer_entry_url = reverse('customer:create_customer')
        cls.customer_email = 'customer@gmail.com'
        cls.volunteer_email = 'v@gmail.com'
        cls.password = 'Test@123'
        cls.url = reverse('help_customer:helped-customer')

    def get_customer_entry(self):
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

    def get_registration_data(self):
        data = {
            "email": '',
            "name": "Rajprabhu",
            "phone_number": "+918757652757",
            "address": "74/24,  velachery, chennai-42",
            "password": self.password,
            "conform_password": self.password,
            "is_volunteer": False,
            "is_customer": False
        }
        return data

    @mock.patch('common.utils')
    def create_customer_volunteer_data(self, mock_utils):
        """Valid Volunteer Register"""
        data = self.get_registration_data()
        data['email'] = self.volunteer_email
        data['is_volunteer'] = True
        # mock response
        mock_utils.map_my_india_api_request.return_value = {
            'longitude': 80,
            'latitude': 13
        }, True
        response = self.client.post(self.resgistration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_volunteer_registration.custom_code)

        """Valid Customer Register"""
        data = self.get_registration_data()
        data['email'] = self.customer_email
        data['is_customer'] = True
        data['phone_number'] = "+918757652756"
        response = self.client.post(self.resgistration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'],
                         common_success_response.success_customer_registration.custom_code)

    def add_customer_entry(self):
        access_token = common_test_functionality.get_customer_access(email=self.customer_email, password=self.password)
        data = self.get_customer_entry()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.post(self.customer_entry_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_data_entry.custom_code)

    def test_invalid_method(self):
        """
        Ensure Invalid Method response
        """
        self.create_customer_volunteer_data()
        self.add_customer_entry()
        access_token = common_test_functionality.get_customer_access(email=self.volunteer_email, password=self.password)
        # self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['custom_code'], common_failure_response.method_not_allowed.custom_code)

    def test_no_order_taken_method(self):
        """
        Ensure Invalid Method response
        """
        self.create_customer_volunteer_data()
        self.add_customer_entry()
        access_token = common_test_functionality.get_customer_access(email=self.volunteer_email, password=self.password)
        # self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['custom_code'],
                         common_failure_response.no_customer_order_taken.custom_code)

    def test_after_order_taken_status(self):
        """
        Ensure Invalid Method response
        """
        self.create_customer_volunteer_data()
        self.add_customer_entry()
        access_token = common_test_functionality.get_customer_access(email=self.volunteer_email, password=self.password)
        # self.url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        entry_created = CustomerDetails.objects.all()[0]
        update_customer_detail_url = reverse('customer:customer-details', kwargs={'uid': entry_created.uid})
        data = self.get_customer_entry()
        response = self.client.patch(update_customer_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_update.custom_code)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['custom_code'], common_success_response.success_customer_location_volunteering.custom_code)

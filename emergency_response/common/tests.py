import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from volunteer.models import Volunteer

# Create your tests here.

url = reverse('token_obtain_pair')


class CommonTestCasesData(APITestCase):
    """Common Functiaobnllity required for multiple testcase"""

    def create_data(self, email='teest@test.com', name='Testing', phone_number='+917452369841', password='Test@123', address='100,100 , velachery, Chennai-42',
                    is_volunteer=False, is_customer=False, is_active=True):
        """Create Volunteer object ie user object"""
        return Volunteer.objects.create_user(name=name, phone_number=phone_number, password=password,
                                             address=address, email=email, is_volunteer=is_volunteer, is_customer=is_customer, is_active=True)

    def get_customer_access(self, email=None, password=None):
        # self.create_data(email=email, password=password)
        """Create Access token for user"""
        client = APIClient()
        response = client.post(url, {"email": email, "password": password}, format='json')
        return response.data['access']


common_test_functionality = CommonTestCasesData()

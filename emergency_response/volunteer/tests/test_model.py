from django.test import TestCase

from common.tests import common_test_functionality
from volunteer.models import (CustomerProfileData, Volunteer,
                              VolunteerProfileData)

# Create your tests here.


class VolunteerTest(TestCase):
    def test_data_entry(self):
        volunteer = common_test_functionality.create_data()
        self.assertTrue(isinstance(volunteer, Volunteer))


class CustomerDetailsTest(TestCase):

    def test_data_entry(self):
        customer = common_test_functionality.create_data(is_customer=True)
        self.assertTrue(isinstance(customer, Volunteer))
        customer_entry = CustomerProfileData.objects.filter(volunteer=customer)
        self.assertEqual(len(customer_entry), 1)

    def test_invalid_data_entry(self):
        customer = common_test_functionality.create_data(is_customer=False)
        self.assertTrue(isinstance(customer, Volunteer))
        customer_entry = CustomerProfileData.objects.filter(volunteer=customer)
        self.assertEqual(len(customer_entry), 0)


class VolunteerDetailsTest(TestCase):

    def test_data_entry(self):
        volunteer = common_test_functionality.create_data(is_volunteer=True)
        self.assertTrue(isinstance(volunteer, Volunteer))
        volunteer_entry = VolunteerProfileData.objects.filter(volunteer=volunteer)
        self.assertEqual(len(volunteer_entry), 1)

    def test_invalid_data_entry(self):
        volunteer = common_test_functionality.create_data(is_volunteer=False)
        self.assertTrue(isinstance(volunteer, Volunteer))
        volunteer_entry = VolunteerProfileData.objects.filter(volunteer=volunteer)
        self.assertEqual(len(volunteer_entry), 0)

from django.test import TestCase

from volunteer.api.v1.serializers import (UpdatePasswordVolunteerSerializer,
                                          VolunteerSerializer)


class CustomerDetailSerializerTest(TestCase):
    """VolunteerSerializer TestCases"""

    def test_validate_data(self):
        """VolunteerSerializer Valid TestCases"""
        data = {
            "email": "rajprabhas123a@egmore.com",
            "name": "Rajprabhu",
            "phone_number": "+918757652757",
            "address": "74/24,  velachery, chennai-42",
            "password": "Rajpabhu@123",
            "conform_password": "Rajpabhu@123",
            "is_volunteer": True
        }
        serializer = VolunteerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_not_valid_data(self):
        """VolunteerSerializer Not Valid TestCases"""
        serializer = VolunteerSerializer(data={})
        self.assertFalse(serializer.is_valid())


class UpdatePasswordVolunteerSerializerTest(TestCase):
    """VolunteerSerializer TestCases"""

    def test_validate_data(self):
        """VolunteerSerializer Valid TestCases"""
        data = {
            "password": "Rajpabhu@123",
            "conform_password": "Rajpabhu@123"
        }
        serializer = UpdatePasswordVolunteerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_not_valid_data(self):
        """VolunteerSerializer Not Valid TestCases"""
        serializer = UpdatePasswordVolunteerSerializer(data={})
        self.assertFalse(serializer.is_valid())

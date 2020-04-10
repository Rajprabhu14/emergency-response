from django.test import TestCase

from customer.models import CustomerDetails
# Create your tests here.


class CustomerDetailsTest(TestCase):
    def create_data(self, name='Rajprabhu', phone_number='+917452369841', grocery={
        'dal': '1kg',
        'vegetable': '0.5kg'
    }, address='100,100 , velachery, Chennai-42', landmark='Test'):
        return CustomerDetails.objects.create(name=name, phone_number=phone_number, grocery=grocery, address=address, landmark=landmark)

    def test_data_entry(self):
        customer = self.create_data()
        self.assertTrue(isinstance(customer, CustomerDetails))

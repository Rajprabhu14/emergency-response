from customer.api.v1.api import CreateCustomer, UpdateCustomerDetailsAPI
from django.urls import path, register_converter, converters
register_converter(converters.UUIDConverter, 'uuid')
app_name = 'customer'

urlpatterns = [
    path('customer', CreateCustomer.as_view(), name='create_customer'),
    path('customer/<uuid:uid>', UpdateCustomerDetailsAPI.as_view(), name='customer-details')
]

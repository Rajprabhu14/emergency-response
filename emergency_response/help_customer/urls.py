from django.urls import path, register_converter
from django.urls.converters import UUIDConverter

from help_customer.api.v1.api import CustomerHelperListAPIView, MyCustomerAPI

register_converter(UUIDConverter, 'uuid')
app_name = 'help_customer'
urlpatterns = [
    path('help/', CustomerHelperListAPIView.as_view(), name='geo-filter-help'),
    path('help/customer/', MyCustomerAPI.as_view(), name='helped-customer')
]

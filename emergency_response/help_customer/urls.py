from django.urls import path, register_converter
from help_customer.api.v1.api import CustomerHelperListAPIView, MyCustomerAPI
from django.urls.converters import UUIDConverter


register_converter(UUIDConverter, 'uuid')
app_name = 'help_customer'
urlpatterns = [
    path('help/<uuid:uid>', CustomerHelperListAPIView.as_view(), name='geo-filter-help'),
    path('help/customer/<uuid:uid>', MyCustomerAPI.as_view(), name='helped-customer')
]

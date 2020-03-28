from customer.api.v1.api import CreateCustomer
from django.urls import path
app_name = 'customer'

urlpatterns = [
    path('customer', CreateCustomer.as_view(), name='create_customer')
]

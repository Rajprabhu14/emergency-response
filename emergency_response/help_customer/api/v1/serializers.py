from customer.models import CustomerDetails
from rest_framework import serializers


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['name', 'phone_number', 'address', 'grocery',
                  'landmark', 'order_status', 'location', 'verfication_completed']

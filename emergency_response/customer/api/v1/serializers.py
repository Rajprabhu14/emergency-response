from customer.models import CustomerDetails, order_choice, default_choice
from rest_framework import serializers


class CustomerDetailSerializer(serializers.ModelSerializer):
    verfication_completed = serializers.BooleanField(write_only=True)
    order_status = serializers.SerializerMethodField()
    location_details = serializers.SerializerMethodField()

    class Meta:
        model = CustomerDetails
        fields = ['uid', 'name', 'phone_number', 'address', 'grocery',
                  'landmark', 'order_status', 'verfication_completed', 'location_details']
        write_only = ('verfication_completed', 'location', 'other_detail')

    def get_order_status(self, obj):
        return obj.get_order_status_display()

    def get_location_details(Self, obj):
        return obj.location.geojson


class ManipulateCustomerDetailSerializer(serializers.ModelSerializer):

    order_status = serializers.ChoiceField(order_choice)
    location_details = serializers.SerializerMethodField()

    class Meta:
        model = CustomerDetails
        fields = ['uid', 'name', 'phone_number', 'address', 'grocery',
                  'landmark', 'order_status', 'location_details']
        # write_only_fields = ('updated_by_id')
        read_only_fields = ('uid', 'name', 'phone_number', 'address', 'grocery', 'landmark')

    def get_location_details(self, obj):
        return obj.location.geojson

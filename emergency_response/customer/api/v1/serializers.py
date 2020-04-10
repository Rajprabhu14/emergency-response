from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from customer.models import CustomerDetails, order_choice


class CustomerDetailSerializer(GeoFeatureModelSerializer):
    verfication_completed = serializers.BooleanField(write_only=True, default=False)
    order_status = serializers.SerializerMethodField()

    class Meta:
        model = CustomerDetails
        geo_field = "location"
        fields = ['uid', 'name', 'phone_number', 'address', 'grocery',
                  'landmark', 'order_status', 'verfication_completed']
        write_only = ('verfication_completed', 'other_detail', 'location')

    def get_order_status(self, obj):
        return obj.get_order_status_display()

    def get_location_details(self, obj):
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

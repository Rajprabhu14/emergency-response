# import json


# from django.conf import settings
# from django.contrib.gis.geos import GEOSGeometry, Point
from django.shortcuts import get_object_or_404
# import requests
# from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.constants import common_failure_response, common_success_response
from common.exceptions import (VolunteerNotActivated,
                               common_failure_response_structure,
                               custom_success_handler)
from common.permissions import IsVolunteerAuthenticated, MethodPermission
from customer.api.v1.serializers import ManipulateCustomerDetailSerializer
from customer.models import CustomerDetails
from volunteer.models import Volunteer


class CustomerHelperListAPIView(ListAPIView):
    """Get the Customer List for Order"""
    serializer_class = ManipulateCustomerDetailSerializer
    parser_classes = [JSONParser]
    lookup_field = 'uid'
    queryset = CustomerDetails.objects.all()
    permission_classes = (MethodPermission, IsVolunteerAuthenticated)
    authentication_classes = (JWTAuthentication, )

    def get_volunteer_queryset(self):
        # Get the volunteer for creating Buffer location query set
        volunteer = Volunteer.objects.filter(verfication_completed=True)
        return volunteer

    # get given volunteer
    def get_volunteer_object(self, request):
        volunteer_query_set = self.get_volunteer_queryset()
        filter = {}
        # for field in self.multiple_lookup_fields:
        filter[self.lookup_field] = request.user.uid
        try:
            obj = get_object_or_404(volunteer_query_set, **filter)
            # self.check_object_permissions(self.request, obj)
            return obj
        except Exception:
            raise VolunteerNotActivated

    # get customer with 11km buffer & no volunteer taken order
    def get_list_queryset(self, request):
        data = self.get_volunteer_object(request)
        # Get user of not alloted customer based on 11.1 km buffer
        q = self.queryset.filter(location__within=data.location.buffer(0.1)).filter(updated_by=None)
        return q

    def get(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.get_list_queryset(request)
        serializer = self.serializer_class(queryset, many=True)
        if len(serializer.data) == 0:
            response = common_failure_response_structure(common_failure_response.customer_data_not_available.message,
                                                         status=common_failure_response.customer_data_not_available.status_code,
                                                         custom_code=common_failure_response.customer_data_not_available.custom_code)
            return Response(response, status=common_failure_response.customer_data_not_available.status_code)
        data = custom_success_handler(serializer.data,
                                      status_code=common_success_response.success_customer_location_volunteering.status_code,
                                      custom_code=common_success_response.success_customer_location_volunteering.custom_code)
        return Response(data, status=common_success_response.success_customer_location_volunteering.status_code)


class MyCustomerAPI(CustomerHelperListAPIView):
    """ Get the Costmer details taken by user"""
    # get customer with volunteer taken order

    def get_list_queryset(self, request):
        q = self.queryset.filter(updated_by=request.user)
        return q

    def get(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.get_list_queryset(request)
        serializer = self.serializer_class(queryset, many=True)
        if len(serializer.data) == 0:
            response = common_failure_response_structure(common_failure_response.no_customer_order_taken.message,
                                                         status=common_failure_response.no_customer_order_taken.status_code,
                                                         custom_code=common_failure_response.no_customer_order_taken.custom_code)
            return Response(response, status=common_failure_response.no_customer_order_taken.status_code)
        data = custom_success_handler(serializer.data,
                                      status_code=common_success_response.success_customer_location_volunteering.status_code,
                                      custom_code=common_success_response.success_customer_location_volunteering.custom_code)
        return Response(data, status=common_success_response.success_customer_location_volunteering.status_code)

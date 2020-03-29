import json

import requests
from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry, Point
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from common.constants import common_failure_response, common_success_response
from common.exceptions import (VolunteerNotActivated,
                               common_failure_response_structure,
                               custom_success_handler)
from customer.api.v1.serializers import CustomerDetailSerializer
from customer.models import CustomerDetails
from volunteer.models import Volunteer
from common.permissions import MethodPermission


class CustomerHelperListAPIView(ListAPIView):
    serializer_class = CustomerDetailSerializer
    parser_classes = [JSONParser]
    multiple_lookup_fields = ['uid']
    queryset = CustomerDetails.objects.all()
    permission_classes = (MethodPermission,)

    def get_volunteer_queryset(self):
        volunteer = Volunteer.objects.filter(verfication_completed=True)
        return volunteer

    # get given volunteer
    def get_volunteer_object(self):
        volunteer_query_set = self.get_volunteer_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]
        try:
            obj = get_object_or_404(volunteer_query_set, **filter)
            # self.check_object_permissions(self.request, obj)
            return obj
        except Exception:
            raise VolunteerNotActivated

    # get customer with 11km buffer & no volunteer taken order
    def get_list_queryset(self):
        data = self.get_volunteer_object()
        q = self.queryset.filter(location__within=data.location.buffer(0.1)).filter(updated_by=None)
        return q

    def get(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.get_list_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if len(serializer.data) == 0:
            response = common_failure_response_structure(common_failure_response.customer_data_not_available.message,
                                                         status=common_failure_response.customer_data_not_available.status_code,
                                                         custom_error_code=common_failure_response.customer_data_not_available.custom_code)
            return Response(response, status=common_failure_response.customer_data_not_available.status_code)
        data = custom_success_handler(serializer.data,
                                      status_code=common_success_response.success_customer_location_volunteering.status_code,
                                      custom_success_code=common_success_response.success_customer_location_volunteering.custom_code)
        return Response(data, status=common_success_response.success_customer_location_volunteering.status_code)


class MyCustomerAPI(CustomerHelperListAPIView):

    # get customer with volunteer taken order
    def get_list_queryset(self):
        data = self.get_volunteer_object()
        q = self.queryset.filter(updated_by=data)
        return q

    def get(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.get_list_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if len(serializer.data) == 0:
            response = common_failure_response_structure(common_failure_response.no_customer_order_taken.message,
                                                         status=common_failure_response.no_customer_order_taken.status_code,
                                                         custom_error_code=common_failure_response.no_customer_order_taken.custom_code)
            return Response(response, status=common_failure_response.no_customer_order_taken.status_code)
        data = custom_success_handler(serializer.data,
                                      status_code=common_success_response.success_customer_location_volunteering.status_code,
                                      custom_success_code=common_success_response.success_customer_location_volunteering.custom_code)
        return Response(data, status=common_success_response.success_customer_location_volunteering.status_code)

import json

import requests
from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from common.constants import common_failure_response, common_success_response
from common.exceptions import common_failure_response_structure, custom_success_handler, CustomerNotActivated
from customer.api.v1.serializers import CustomerDetailSerializer, ManipulateCustomerDetailSerializer
from customer.models import CustomerDetails
from django.shortcuts import get_object_or_404

class CreateCustomer(CreateAPIView):
    serializer_class = CustomerDetailSerializer
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            response = common_failure_response_structure(serializer.errors,
                                                         status=common_failure_response.validation_error.status_code,
                                                         custom_error_code=common_failure_response.validation_error.custom_codew)
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # Get data for location
        settings.MAP_MY_INDIA__PARAMS['address'] = serializer.validated_data['address']
        r = requests.get(url=settings.MAP_MY_INDIA_URL, params=settings.MAP_MY_INDIA__PARAMS)
        if r.status_code == 200:
            # location obtain from mapmy india api call
            data = json.loads(r.json()['data'][0])
            point = Point(data['copResults']['longitude'], data['copResults']['latitude'], srid=4326)
            request.data.update({'location': point})
            self.create(request)
            data = custom_success_handler(common_success_response.success_customer_data_entry.message,
                                          status_code=common_success_response.success_customer_data_entry.status_code,
                                          custom_success_code=common_success_response.success_customer_data_entry.custom_code)
            return Response(data, status=common_success_response.success_customer_data_entry.status_code)
        else:
            # error retrieval for api
            # logger adding(r.json())
            response = common_failure_response_structure(common_failure_response.location_creation_error.messages,
                                                         status=common_failure_response.location_creation_error.status_code,
                                                         custom_error_code=common_failure_response.location_creation_error.custom_code)
            return Response(response, status=common_failure_response.location_creation_error.status_code)


class UpdateCustomerDetailsAPI(RetrieveUpdateAPIView):
    serializer_class = ManipulateCustomerDetailSerializer
    parser_classes = [JSONParser]
    queryset = CustomerDetails.objects.all()
    lookup_field = 'uid'

    def get_object(self):
        query_set = self.get_queryset()
        filter = {}
        # for field in self.multiple_lookup_fields:
        filter[self.lookup_field] = self.kwargs[self.lookup_field]
        try:
            obj = get_object_or_404(query_set, **filter)
            # self.check_object_permissions(self.request, obj)
            return obj
        except Exception:
            raise CustomerNotActivated
    def perform_update(self, serializer):
        if self.request.user.is_anonymous:
            serializer.save(updated_by=None)
        else:
            serializer.save(updated_by=self.request.user)

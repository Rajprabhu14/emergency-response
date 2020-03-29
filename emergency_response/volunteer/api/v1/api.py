import json

import requests
from django.conf import settings
from django.contrib.gis.geos import Point
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (CreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from common.constants import common_failure_response, common_success_response
from common.exceptions import (common_failure_response_structure,
                               custom_success_handler)
from common.permissions import (CustomPermissionRules,
                                CustomPostDjangoPermission,
                                CustomVolunteeringDjangoPermission,
                                IsOwnerOrReadOnly)
from volunteer.api.v1.serializers import (ManipulateVolunteerSerializer,
                                          UpdatePasswordVolunteerSerializer,
                                          VolunteerSerializer)
from volunteer.models import Volunteer


class CreateVolunteerAPI(CreateAPIView):
    """"API for Creating Volunteers"""
    serializer_class = VolunteerSerializer
    parser_classes = [JSONParser]
    # permission_classes = (CustomPermissionRules)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            response = common_failure_response_structure(serializer.errors,
                                                         status=common_failure_response.validation_error.status_code,
                                                         custom_error_code=common_failure_response.validation_error.custom_code)
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # Get data for location
        settings.MAP_MY_INDIA__PARAMS['address'] = serializer.validated_data['address']
        r = requests.get(url=settings.MAP_MY_INDIA_URL, params=settings.MAP_MY_INDIA__PARAMS)
        if r.status_code == 200:
            # location obtain from mapmy india api call
            data = json.loads(r.json()['data'][0])
            point = Point(data['copResults']['longitude'], data['copResults']['latitude'], srid=4326)
            request.data.update({'location': point})
            # serializer.validated_data.update({'location': point})
            # serializer.save()
            self.create(request)
            data = custom_success_handler(common_success_response.success_volunteer_registration,
                                          status_code=common_success_response.success_volunteer_registration.status_code,
                                          custom_success_code=common_success_response.success_volunteer_registration.custom_code)
            return Response(data, status=common_success_response.success_volunteer_registration.status_code)
        else:
            # error retrieval for api
            # logger adding(r.json())
            response = common_failure_response_structure(common_failure_response.location_creation_error.message,
                                                         status=common_failure_response.location_creation_error.status_code,
                                                         custom_error_code=common_failure_response.location_creation_error.custom_code)
            return Response(response, status=common_failure_response.location_creation_error.status_code)


class ManipulateVolunteerAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = ManipulateVolunteerSerializer
    queryset = Volunteer.objects.all()
    multiple_lookup_fields = ['uid']
    # permission_classes = (IsOwnerOrReadOnly),

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateVolunteerPassword(UpdateAPIView):
    serializer_class = UpdatePasswordVolunteerSerializer
    queryset = Volunteer.objects.all()
    multiple_lookup_fields = ['uid']
    # permission_classes = (IsOwnerOrReadOnly),

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            response = common_failure_response_structure(serializer.errors,
                                                         status=common_failure_response.validation_error.status_code,
                                                         custom_error_code=common_failure_response.validation_error.custom_code)
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.update(request)
        data = custom_success_handler(common_success_response.success_volunteer_password,
                                      status_code=common_success_response.success_volunteer_password.status_code,
                                      custom_success_code=common_success_response.success_volunteer_password.custom_code)
        return Response(data, status=common_success_response.success_volunteer_password.status_code)

from django.shortcuts import render
from common.exceptions import common_failure_response_structure
from common.constants import common_failure_response
from django.http import JsonResponse
from rest_framework import status
# Create your views here.


def response_404(request, *args, **kwargs):

    # return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    response = common_failure_response_structure(common_failure_response.url_not_found.message,
                                                 status=common_failure_response.url_not_found.status_code,
                                                 custom_error_code=common_failure_response.url_not_found.custom_code)
    return JsonResponse(response, status=common_failure_response.url_not_found.status_code)

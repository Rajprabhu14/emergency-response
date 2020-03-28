from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


def custom_response_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response.result = response.data['detail']
    return response


def custom_success_handler(data, status_code=status.HTTP_200_OK, custom_success_code=15001):
    return {
        'status_code': status_code,
        'custom_success_code': custom_success_code,
        'status': 'success',
        'result': data.message
    }


def common_failure_response_structure(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, custom_error_code=191919):
    return {
        'status_code': status,
        'status': 'failure',
        'custom_error_code': custom_error_code,
        'result': data
    }

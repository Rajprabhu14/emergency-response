from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

from common.constants import common_failure_response


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class CUSTOMURLNOTFOUND(APIException):
    status_code = common_failure_response.url_not_found.status_code
    custom_code = common_failure_response.url_not_found.custom_code
    default_code = common_failure_response.url_not_found.default_code
    default_detail = common_failure_response.url_not_found.message


class CustomMethodNotAllowed(APIException):
    status_code = common_failure_response.method_not_allowed.status_code
    custom_code = common_failure_response.method_not_allowed.custom_code
    default_code = common_failure_response.method_not_allowed.default_code
    default_detail = common_failure_response.method_not_allowed.message


class VolunteerNotActivated(APIException):
    status_code = common_failure_response.incorrect_volunteer_uid.status_code
    custom_code = common_failure_response.incorrect_volunteer_uid.custom_code
    default_detail = common_failure_response.incorrect_volunteer_uid.message
    default_code = common_failure_response.incorrect_volunteer_uid.default_code


class CustomerNotActivated(APIException):
    status_code = common_failure_response.incorrect_customer_uid.status_code
    custom_code = common_failure_response.incorrect_customer_uid.custom_code
    default_detail = common_failure_response.incorrect_customer_uid.message
    default_code = common_failure_response.incorrect_customer_uid.default_code


def custom_response_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response.result = response.data['detail']
    return response


def custom_success_handler(data, status_code=status.HTTP_200_OK, custom_code=15001):
    return {
        'status_code': status_code,
        'custom_code': custom_code,
        'status': 'success',
        'result': data
    }


def common_failure_response_structure(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, custom_code=191919):
    return {
        'status_code': status,
        'status': 'failure',
        'custom_code': custom_code,
        'result': data
    }


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    data = dict()
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None and exc is not None:
        data['status_code'] = exc.status_code
        data['status'] = 'failure'
        data['result'] = exc.detail
        if exc.custom_code:
            data['custom_code'] = exc.custom_code
        response.data = data
    return response

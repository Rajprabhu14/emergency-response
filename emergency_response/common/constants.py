from django.utils.translation import gettext_lazy as _
from dotmap import DotMap
from rest_framework import status
common_success_response = DotMap(
    success_customer_data_entry=DotMap(message=_('Request submited. You will receive call shortly'),
                                       status_code=status.HTTP_201_CREATED,
                                       custom_code='15001'),
    success_volunteer_registration=DotMap(message=_('Volunteering registered. You will receive call shortly'),
                                          status_code=status.HTTP_201_CREATED,
                                          custom_code='15002'),
    success_volunteer_password=DotMap(message=_('Password Updated'),
                                      status_code=status.HTTP_200_OK,
                                      custom_code='15003'),
    success_customer_location_volunteering=DotMap(message=_('Success'),
                                                  status_code=status.HTTP_200_OK,
                                                  custom_code='15004'),
)

common_failure_response = DotMap(
    validation_error=DotMap(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            default_code='VALIDATION_ERROR',
                            custom_code='19001'),
    location_creation_error=DotMap(message=_('API Error or unable to get address'),
                                   default_code='MAP_API_ERROR',
                                   status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                   custom_code='19002'),
    customer_data_not_available=DotMap(message=_('No customer available from your location'),
                                       default_code='CUSTOMR_NOT_PRESENT',
                                       status_code=status.HTTP_417_EXPECTATION_FAILED,
                                       custom_code='19003'),
    incorrect_volunteer_uid=DotMap(message=_('Invalid Volunteer'),
                                   status_code=status.HTTP_401_UNAUTHORIZED,
                                   default_code='VOLUNTEER_NOT_PRESENT',
                                   custom_code='19004'),
)

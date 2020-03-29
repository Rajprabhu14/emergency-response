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
)

common_failure_response = DotMap(
    validation_error=DotMap(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            custom_code='19001'),
    location_creation_error=DotMap(message=_('API Error or unable to get address'),
                                   status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                   custom_code='19002'),
)

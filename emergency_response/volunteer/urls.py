from django.urls import path, register_converter
from django.urls.converters import UUIDConverter

from volunteer.api.v1.api import CreateVolunteerAPI, ManipulateVolunteerAPI, UpdateVolunteerPassword
register_converter(UUIDConverter, 'uuid')
app_name = 'volunteer'
urlpatterns = [
    path('volunteer/', CreateVolunteerAPI.as_view(), name='volunteer'),
    path('volunteer/<uuid:uid>', ManipulateVolunteerAPI.as_view(), name='volunteer-detail'),
    path('volunteer/update/<uuid:uid>', UpdateVolunteerPassword.as_view(), name='volunteer-password-update')
]

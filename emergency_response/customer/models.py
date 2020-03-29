import uuid

from django.contrib.gis.db import models as geo_models
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.conf import settings
from volunteer.models import Volunteer
# Create your models here.

default_choice = 'N'
Unreachable = settings.UNREACHABLE_CUSTOMER
order_choice = [
    (default_choice, 'Not Verified'),
    ('V', 'Verified'),
    ('T', 'Taken'),
    ('I', 'InTransit'),
    ('D', 'Deliveried'),
    (Unreachable, 'unreachable')
]


class CustomerDetails(models.Model):

    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    grocery = JSONField()
    landmark = models.CharField(max_length=255)
    order_status = models.CharField(max_length=2,
                                    choices=order_choice,
                                    default=default_choice)
    location = geo_models.PointField(srid=4326, spatial_index=True, blank=True, null=True)
    verfication_completed = models.BooleanField(default=False)
    other_detail = models.TextField(blank=True, null=True)
    updated_by = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-verfication_completed']
        db_table = 'customer_details'

    def __str__(self):
        return 'Name- %s - phone_number - %s status-%s' % (self.name, self.phone_number, str(self.verfication_completed))

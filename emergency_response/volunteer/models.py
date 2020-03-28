import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.gis.db import models as geo_models
from django.db import models
from volunteer.manager import CustomVolunteerManager
# Create your models here.


class Volunteer(AbstractBaseUser):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    address = models.CharField(max_length=500, null=False, blank=False)
    location = geo_models.PointField(srid=4326, spatial_index=True, blank=True, null=True)
    verfication_completed = models.BooleanField(default=False)
    other_details = models.TextField(blank=True, null=True)

    objects = CustomVolunteerManager()

    class Meta:
        ordering = ['-verfication_completed']
        db_table = 'volunteer_detail'

    def __str__(self):
        return 'Name- %s - phone_number - %s status-%s' % (self.name, self.phone_number, str(self.verfication_completed))

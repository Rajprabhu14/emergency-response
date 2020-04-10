import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.gis.db import models as geo_models
from django.db import models
from django.utils import timezone

from volunteer.manager import CustomVolunteerManager

# Create your models here.


# class Volunteer(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     email = models.EmailField(unique=True, blank=False, null=False)
#     name = models.CharField(max_length=100, null=False, blank=False)
#     phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
#     address = models.CharField(max_length=500, null=False, blank=False)
#     location = geo_models.PointField(srid=4326, spatial_index=True, blank=True, null=True)
#     verfication_completed = models.BooleanField(default=False)
#     other_details = models.TextField(blank=True, null=True)
#     password = models.CharField(max_length=128, null=False, blank=False)
#     objects = CustomVolunteerManager()

#     class Meta:
#         ordering = ['-verfication_completed']
#         db_table = 'volunteer_detail'

#     def __str__(self):
#         return 'Name- %s - phone_number - %s status-%s' % (self.name, self.phone_number, str(self.verfication_completed))


# class User(AbstractUser):
#     is_volunteer = models.BooleanField(default=False)


class Volunteer(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name', 'phone_number', 'address')
    # username = models.CharField()
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    address = models.CharField(max_length=500, null=False, blank=False)
    location = geo_models.PointField(srid=4326, spatial_index=True, blank=True, null=True)
    verfication_completed = models.BooleanField(default=False)
    other_details = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_volunteer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomVolunteerManager()

    ordering = ['-verfication_completed']

    class Meta:
        db_table = 'volunteer_detail'

    def __str__(self):
        return 'Name- %s - phone_number - %s status-%s' % (self.name, self.phone_number, str(self.verfication_completed))


class CustomerProfileData(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'customer_profile_table'

    def __str__(self):
        return '{}'.format(self.volunteer.email)


class VolunteerProfileData(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_profile_table'

    def __str__(self):
        return '{}'.format(self.volunteer.email)

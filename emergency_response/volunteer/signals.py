from django.db.models.signals import post_save
from django.dispatch import receiver

from volunteer.models import (CustomerProfileData, Volunteer,
                              VolunteerProfileData)


@receiver(post_save, sender=Volunteer)
def update_profile_type(sender, instance, **kwargs):
    """Function updating the different user profile """
    if instance.is_volunteer:
        VolunteerProfileData.objects.create(volunteer=instance)

    if instance.is_customer:
        CustomerProfileData.objects.create(volunteer=instance)

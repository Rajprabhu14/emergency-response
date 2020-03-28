from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomVolunteerManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        # print(**extra_fields)
        volunteer = self.model(email=email, **extra_fields)
        volunteer.password = make_password(password)
        volunteer.save()
        return volunteer

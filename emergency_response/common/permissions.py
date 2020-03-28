from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, DjangoModelPermissions


class CustomVolunteeringDjangoPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['PUT'] = ['%(app_label)s.view_%(model_name)s']


class CustomPostDjangoPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['POST'] = ['%(app_label)s.view_%(model_name)s']


class CustomPermissionRules(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and isinstance(request.user, AnonymousUser):
            return True
        elif (not request.auth) and (request.method == 'PUT' or request.method == 'GET'):
            return True
        else:
            return False

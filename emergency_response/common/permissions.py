from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import (BasePermission, DjangoModelPermissions,
                                        IsAuthenticated)

from common.exceptions import CustomMethodNotAllowed


class CustomVolunteeringDjangoPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['PUT'] = ['%(app_label)s.view_%(model_name)s']


class CustomPostDjangoPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['POST'] = ['%(app_label)s.view_%(model_name)s']


class CustomPermissionRules(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method == 'POST' and isinstance(request.user, AnonymousUser):
            return True
        elif (not request.auth) and (request.method == 'PUT' or request.method == 'GET'):
            return True
        else:
            return False


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.id == request.user.id


class MethodPermission(BasePermission):
    """ Generic Method allowed permission class"""

    def has_permission(self, request, view):
        if request.method in view.allowed_methods:
            return True
        else:
            raise CustomMethodNotAllowed


class IsCustomerAuthenticated(BasePermission):
    """
    Allows access only to authenticated Customer users.
    """

    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated and request.user.is_customer) or request.user.is_superuser)


class IsVolunteerAuthenticated(BasePermission):
    """
    Allows access only to authenticated Volunteer users.
    """

    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated and request.user.is_volunteer) or request.user.is_superuser)

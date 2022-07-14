from rest_framework import permissions
from rest_framework.generics import get_object_or_404





class IsProfileFieldFromCurrentUser(permissions.BasePermission):
    """
    Object-level permission to only allow profileOwner of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance profile must be the profile from current user
        return obj.profile == request.user.profile

class IsAddressOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Instance profile must be the profile from current user
        return obj.profile == request.user.profile

class IsProfileOwner(permissions.BasePermission):
    """
    Object-level permission to only allow profileOwner of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance profile must be the profile from current user
        return obj.user == request.user

class IsUserOwner(permissions.BasePermission):
    """
    Object-level permission to only allow obj owner
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
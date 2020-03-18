from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsOwnerOrAdminPermission(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        if hasattr(obj, 'owner'):
            return (obj.owner == request.user) or request.user.is_staff
        else:
            return request.user.is_staff

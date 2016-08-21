from rest_framework import permissions


class IsAdminOrSelfPostAnyone(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Limit access to exact instances, users can access only them selves.
        """
        return request.user and (request.user.is_staff or request.user == obj)

from rest_framework import permissions


class IsAdminOrOwnerPostAnyone(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Limit access to exact instances, owners can access only their instances.
        """
        if not request.user:
            return False
        elif request.user.is_staff:
            return True
        elif hasattr(obj, 'user'):
            return request.user == obj.user
        elif hasattr(obj, 'student'):
            return request.user == obj.student.user
        return False

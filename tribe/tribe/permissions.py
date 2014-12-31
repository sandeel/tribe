from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """ 

    def has_permission(self, request, view):
        if (request.method == "POST") or (request.user.is_superuser):
            return True

        return False

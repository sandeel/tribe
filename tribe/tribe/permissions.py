from rest_framework import permissions

SAFE_METHODS = ['POST',]

class IsAuthenticatedOrPost(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS):
            return True
        return False

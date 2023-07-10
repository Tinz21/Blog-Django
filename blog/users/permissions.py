""" Users permissions """

from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.kwargs['username'] == request.user.username \
                or request.user.is_superuser:
            return True
        else:
            return False

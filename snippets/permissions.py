# permissions.py

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    '''
    Custom permissions for editing owner only
    '''

    def has_object_permission(self, request, view, obj):
        #we are allowting read permissions for all requests.

        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions are only allowed to the owner of this snippet.
        return obj.owner == request.user

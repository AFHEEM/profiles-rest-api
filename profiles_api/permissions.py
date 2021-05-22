from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profile
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if user has permission to edit profile
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """
    Allow users to edit their own status
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if user has permission to edit his own status
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        # Foreign key user_profile.id to check if feed is edited by the same user using token
        return obj.user_profile.id == request.user.id

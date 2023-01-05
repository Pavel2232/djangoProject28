from rest_framework import permissions

from user.models import User

class UserUpdatePermission(permissions.BasePermission):
    message = 'Вы не можете изменить объявление.'

    def has_object_permission(self, request, view, obj):
        if request.user.role != User.ADMIN:
            return obj.author == request.user
        return True



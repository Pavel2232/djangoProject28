from rest_framework import permissions

from user.models import User

class UserPermission(permissions.BasePermission):
    message = 'Вы не можете изменить объявление.'

    def has_object_permission(self, request, view, obj):
        if request.user.role != User.ADMIN:
            return obj.author == request.user
        return True


class UserPathchrmission(permissions.BasePermission):
    message = 'Вы не можете изменить чужую подборку'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user



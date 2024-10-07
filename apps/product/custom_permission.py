from django.contrib.auth import admin
from rest_framework import  permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        # return request.user.is_staff # проверка на пользователя зарегованного и на админство    #| =
        elif request.user.is_staff:                                                       #        | same things yeah
            return True                                                                   #        | =

class IsActiveOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        # return request.user.is_staff # проверка на пользователя активного и на админство         #| =
        elif request.user.is_active:                                                       #        | same things yeah
            return True                                                                   #         | =

class IsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
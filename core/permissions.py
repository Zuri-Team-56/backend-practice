from django.contrib.auth.backends import ModelBackend
from rest_framework.permissions import IsAdminUser as BaseIsAdminUser
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commenter == request.user


class UserAdmin(BaseIsAdminUser, ModelBackend):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return super().has_object_permission(request, view, obj)

    def _allow_edit(self, obj=None):
        if not obj:
            return True
        return not (obj.is_staff or obj.is_superuser)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
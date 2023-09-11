from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    group_name = 'admins'

    def has_permission(self, request, view):
        return request.user.groups.filter(name=self.group_name).exists()


class UserPermission(BasePermission):
    ...


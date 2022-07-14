from django.db import models
from core.models.User import User
from django.conf import settings
from dry_rest_permissions.generics import authenticated_users
from core.permissions.ProfilePermission import ProfilePermission as perm
from reservation.models.Table import Table


class Seat(models.Model):
    name = models.CharField(max_length=200, blank="True", null=True)
    table = models.ForeignKey(Table, related_name="table", on_delete=models.CASCADE, blank=True)


    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seat'

    def __str__(self):
        return self.name

    @staticmethod
    @authenticated_users
    def has_read_permission(request):
        return True
    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return False

    @authenticated_users
    def has_object_read_permission(self, request):
        return True

    @authenticated_users
    def has_object_write_permission(self, request):
        return perm.is_user_owner(request, self)

    @authenticated_users
    def has_object_update_permission(self, request):
        return perm.is_user_owner(request, self)
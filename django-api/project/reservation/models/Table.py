from django.db import models
from core.models.User import User
from django.conf import settings
from dry_rest_permissions.generics import authenticated_users
from core.permissions.ProfilePermission import ProfilePermission as perm
from reservation.models.Restaurant import Restaurant
from reservation.models.Reservation import Reservation


class Table(models.Model):
    name = models.CharField(max_length=200, blank="True", null=True)
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant", on_delete=models.CASCADE, blank=True)
    reservation = models.ForeignKey(Reservation, related_name="reservation", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Table'

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
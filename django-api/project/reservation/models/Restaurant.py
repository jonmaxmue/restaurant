from django.db import models
from django.conf import settings
from dry_rest_permissions.generics import authenticated_users
from core.permissions.ProfilePermission import ProfilePermission as perm

class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank="True", null=True)
    created = models.DateTimeField(auto_now_add=True)

    '''
    gender = models.CharField(
        max_length=20,
        choices=(('Male', 'Männer'), ('Female', 'Frauen')),
        null=True,
        blank=True
    )
    '''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurant'

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
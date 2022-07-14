from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from core.models.UserManager import UserManager
from core.models.Authorization import Authorization
from dry_rest_permissions.generics import authenticated_users

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    authorization = models.OneToOneField(Authorization, related_name="user", on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    #REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        Simplest possible answer: All admins are staff
        """
        return self.is_admin

    # has to do with admin backend
    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        Simplest possible answer: Yes, always
        """
        return True

    # has to do with admin backend
    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        Simplest possible answer: Yes, always
        """
        return True

    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzer'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)


    def get_username(self):
        return self.username

    @staticmethod
    @authenticated_users
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    @staticmethod
    def has_create_permission(request):
        return True

    @authenticated_users
    def has_object_read_permission(self, request):
        return request.user.id == self.id

    @authenticated_users
    def has_object_write_permission(self, request):
        return request.user.id == self.id

    @authenticated_users
    def has_object_update_permission(self, request):
        return request.user.id == self.id

from django.db import models
from core.models.User import User
from core.models.Address import Address
from django.conf import settings
from dry_rest_permissions.generics import authenticated_users
from project.models.ImageQualityHandler import ImageQualityHandler
from project.models.UploadDirectory import UploadDirectory
from project.models.HandleFilePath import HandleFilePath
from project.models.MailJet import MailJet

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    street = models.CharField(max_length=30, blank=False, null=False)
    house = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    phone = models.CharField(max_length=30, blank=False, null=False)
    message = models.CharField(max_length=30, blank=False, null=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

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
        return True #perm.is_user_owner(request, self)

    @authenticated_users
    def has_object_update_permission(self, request):
        return True #perm.is_user_owner(request, self)
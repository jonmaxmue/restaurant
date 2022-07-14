from django.db import models
from core.models.User import User
from core.models.Address import Address
from django.conf import settings
from dry_rest_permissions.generics import authenticated_users
from project.models.ImageQualityHandler import ImageQualityHandler
from project.models.UploadDirectory import UploadDirectory
from project.models.HandleFilePath import HandleFilePath
from project.models.MailJet import MailJet
from core.permissions.ProfilePermission import ProfilePermission as perm

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=UploadDirectory("profiles"), null=True, blank=True)
    is_preacher = models.BooleanField(blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=(('Male', 'Männer'), ('Female', 'Frauen')),
        null=True,
        blank=True
    )
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="profile")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.avatar:
            saved_avatar = Profile.objects.get(pk=self.id).avatar
            if saved_avatar != self.avatar:
                image_qh = ImageQualityHandler(self.avatar, settings.AVATAR_LONGEST_SIDE, settings.AVATAR_QUALITY)
                uploaded = image_qh.get_InMemoryUploadedFile()
                self.avatar = uploaded
            else:
                self.avatar = saved_avatar
        super(Profile, self).save(*args, **kwargs)

    def get_full_name(self):
        return " ".join([self.firstname, self.lastname])

    def get_first_name(self):
        return self.firstname

    def get_short_name(self):
        return self.username

    def get_avatar(self, obj):
        if obj.avatar:
            file_url = obj.avatar.url
            return HandleFilePath.build_absolute_uri(file_url)
        return None

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_bio(self):
        return self.bio

    def notify_update(self, message):
        return MailJet().send_mail_with_update_message(self.user.email, self.get_full_name, message)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profile'

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
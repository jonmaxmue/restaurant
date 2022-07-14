from rest_framework_json_api import serializers as serializerJsonApi
from core.models import Profile
from rest_framework_json_api.relations import ResourceRelatedField, HyperlinkedRelatedField
from core.permissions.ProfilePermission import ProfilePermission
from project.models.SerializerPermission import SerializerPermission

class ProfileSerializer(serializerJsonApi.HyperlinkedModelSerializer):
    username = serializerJsonApi.SerializerMethodField('get_username')
    age = serializerJsonApi.SerializerMethodField('get_age')
    date_of_birth = serializerJsonApi.SerializerMethodField('get_date_of_birth')

    def __init__(self, *args, **kwargs):
        super(ProfileSerializer, self).__init__(*args, **kwargs)
        self.permissions = SerializerPermission(ProfilePermission, self.context)

    def get_username(self, obj):
        if self.permissions.is_user_or_manager(obj):
            return obj.user.username

    def get_age(self, obj):
        if self.permissions.is_user_or_manager(obj):
            return obj.age

    def get_date_of_birth(self, obj):
        if self.permissions.is_user_or_manager(obj):
            return obj.date_of_birth

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'firstname', 'lastname', 'date_of_birth',
            'avatar', 'is_preacher', 'age', 'gender', 'created',
            'address', 'address_id', 'user', 'username', 'url'
        ]

    class JSONAPIMeta:
        resource_name = "Profile"

class ProfileAvatarSerializer(serializerJsonApi.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['avatar']

    class JSONAPIMeta:
        resource_name = "Profile"

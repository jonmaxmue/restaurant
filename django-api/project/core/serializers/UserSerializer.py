#from push_notifications.models import APNSDevice
from rest_framework_json_api import serializers as serializerJsonApi
from django.contrib.auth import get_user_model
from core.serializers.ProfileSerializer import ProfileSerializer
from core.models.Authorization import Authorization

class UserSerializer(serializerJsonApi.HyperlinkedModelSerializer):
    #password_confirm = serializers.CharField(write_only=True)

    #TODO
    #apns_device_token = serializerJsonApi.SerializerMethodField()

    code = serializerJsonApi.CharField(write_only=True)
    password = serializerJsonApi.CharField(write_only=True)

    included_serializers = {
        'profile': ProfileSerializer,
    }

    def get_apns_device_token(self, obj):
        # TODO use DjangoUserAgents plugin to detect in request IOS OR ANDROID ....
        # then send the correct token to check on client side if the curent device token ist set
        user_device = False
        try:
            user_device = APNSDevice.objects.filter(user=obj)
        except Exception as e:
            pass
        return True if user_device else False


    def validate_password(self, data):
        '''
        if data['password'] != data['password_confirm']:
            raise serializerJsonApi.ValidationError('Passwords must match.')
        '''
        return data


    def validate_code(self, code):
        try:
            authorization = Authorization.objects.get(
                code=code,
                user__id=self.initial_data["id"]
            )
        except Exception:
            raise serializerJsonApi.ValidationError({"code": "Hast du den Code richtig eingegeben?"})
        return code

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password', 'password_confirm')
        }
        data['password'] = validated_data['password']
        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = ['profile', 'username', 'phone_number', 'email', 'code', 'password', 'url']
        read_only_fields = ['id', 'username']

    class JSONAPIMeta:
        resource_name = "User"
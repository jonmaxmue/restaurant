from rest_framework_json_api import serializers as serializerJsonApi
from core.models import Authorization

class AuthorizationSerializer(serializerJsonApi.ModelSerializer):

    class Meta:
        model = Authorization
        fields = '__all__'
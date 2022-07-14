from rest_framework_json_api import serializers as serializerJsonApi

from core.models.Contact import Contact


class ContactSerializer(serializerJsonApi.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ContactSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = '__all__'

    class JSONAPIMeta:
        resource_name = "Contact"
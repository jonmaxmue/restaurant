from rest_framework_json_api import serializers as serializerJsonApi
from reservation.models import Table

class TableSerializer(serializerJsonApi.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super(TableSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Table
        fields = '__all__'

    class JSONAPIMeta:
        resource_name = "Table"
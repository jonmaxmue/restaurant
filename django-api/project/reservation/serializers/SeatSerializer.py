from rest_framework_json_api import serializers as serializerJsonApi
from reservation.models import Seat

class SeatSerializer(serializerJsonApi.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super(SeatSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Seat
        fields = '__all__'

    class JSONAPIMeta:
        resource_name = "Seat"
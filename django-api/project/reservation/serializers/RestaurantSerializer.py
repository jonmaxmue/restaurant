from rest_framework_json_api import serializers as serializerJsonApi
from reservation.models import Restaurant

class RestaurantSerializer(serializerJsonApi.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super(RestaurantSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Restaurant
        fields = '__all__'

    class JSONAPIMeta:
        resource_name = "Restaurant"
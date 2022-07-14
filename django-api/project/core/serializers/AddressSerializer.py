from rest_framework_json_api import serializers as serializerJsonApi
from core.models import Address
from django.contrib.gis.geos.point import Point
import json


class AddressSerializer(serializerJsonApi.ModelSerializer):

    def create(self, validated_data):
        if type(validated_data['geo_point']) == type({}):
            long = validated_data['geo_point']['longitude']
            lat = validated_data['geo_point']['latitude']
        else:
            jCoords = json.loads(validated_data['geo_point'])
            long = float(jCoords[0].replace(',', '.'))
            lat = float(jCoords[1].replace(',', '.'))
        validated_data['geo_point'] = Point(long, lat)
        address = Address.objects.update_or_create(**validated_data)
        return address[0]

    def update(self, instance, validated_data):
        point = Point(validated_data['geo_point']['longitude'], validated_data['geo_point']['latitude'])

        instance.plz = validated_data.get('plz', instance.plz)
        instance.street = validated_data.get('street', instance.street)
        instance.house = validated_data.get('house', instance.house)
        instance.geo_point = point
        instance.save()
        return instance

    class Meta:
        model = Address
        fields = '__all__'
        extra_kwargs = {"plz": {"required": False, "allow_null": True}, "geo_point": {"required": False, "allow_null": True}}

    class JSONAPIMeta:
        resource_name = "Address"
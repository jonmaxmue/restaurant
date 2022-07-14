from dry_rest_permissions.generics import DRYPermissions
from rest_framework_json_api import views
from reservation.serializers.RestaurantSerializer import RestaurantSerializer
from reservation.models.Restaurant import Restaurant

class RestaurantViewSet(views.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'GET':
            #return [DRYPermissions(),]
            pass
        return []
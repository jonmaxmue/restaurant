from dry_rest_permissions.generics import DRYPermissions
from rest_framework_json_api import views
from reservation.serializers.SeatSerializer import SeatSerializer
from reservation.models.Seat import Seat

class SeatViewSet(views.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'GET':
            #return [DRYPermissions(),]
            pass
        return []
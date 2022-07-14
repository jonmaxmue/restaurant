from dry_rest_permissions.generics import DRYPermissions
from rest_framework_json_api import views
from reservation.serializers.TableSerializer import TableSerializer
from reservation.models.Seat import Table

class TableViewSet(views.ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'GET':
            #return [DRYPermissions(),]
            pass
        return
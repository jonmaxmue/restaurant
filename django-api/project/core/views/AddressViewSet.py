from rest_framework import permissions, status, viewsets
from core.serializers.AddressSerializer import AddressSerializer
from rest_condition import And, Or, Not
#from project.Permissions import IsReadyOnlyRequest, IsPostRequest, IsPutRequest, IsPatchRequest, IsDeleteRequest
from rest_framework.permissions import IsAuthenticated
from core.models.Address import Address

class AddressViewSet(viewsets.ModelViewSet):

    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.all()
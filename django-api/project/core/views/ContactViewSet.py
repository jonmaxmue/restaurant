from rest_framework import status, decorators
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import response
from dry_rest_permissions.generics import DRYPermissions

from rest_framework_json_api import views

from core.models.Contact import Contact
from core.serializers.ContactSerializer import ContactSerializer


class ContactViewSet(views.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [DRYPermissions(),]
        return []
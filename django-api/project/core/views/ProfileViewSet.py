from rest_framework import status, decorators
from core.serializers.ProfileSerializer import ProfileSerializer, ProfileAvatarSerializer
from core.models.Profile import Profile
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import response
from dry_rest_permissions.generics import DRYPermissions

from rest_framework_json_api import views

class ProfileViewSet(views.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'GET':
            return [DRYPermissions(),]
        return []

    @decorators.action(
        detail=True,
        methods=['PATCH'],
        serializer_class=ProfileAvatarSerializer,
        parser_classes=[MultiPartParser],
    )
    def avatar(self, request):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

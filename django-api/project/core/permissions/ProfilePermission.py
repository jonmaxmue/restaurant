from rest_framework import permissions
from django.db.models import Q
from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissionFiltersBase


class ProfilePermission:


    @staticmethod
    def is_user_owner(request, obj):
        return obj.user == request.user


class ProfilePermissionListFilter(DRYPermissionFiltersBase):

    def filter_list_queryset(self, request, queryset, view):
        """
        Limits all list requests to only be seen by the owners or creators.
        """
        #return queryset.filter(Q(owner=request.user) | Q(creator=request.user)) # TODO LOOK HERE HOW IT WORKS
        #q = queryset.filter(Q(community_relation__profile=request.user.profile)) # TODO NOT CORRECT
        return queryset
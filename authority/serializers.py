from django.contrib.contenttypes.models import ContentType
from .models import *
from django.contrib.auth.models import Group
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)


class PermissionSerializer(ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

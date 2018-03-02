from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework import permissions
from django.contrib.auth.decorators import login_required
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import *


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class GroupCreateAPIView(LoginRequiredMixin, CreateAPIView):
    serializer_class = GroupCreateSerializer
    queryset = Group.objects.all()


class GroupListAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all()


class GroupDetailAPIView(LoginRequiredMixin,
                         DestroyModelMixin,
                         UpdateModelMixin,
                         generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = GroupDetailSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = GroupDetailSerializer(
            group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            group = self.get_object(pk)
            group.delete()
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)


class BioCreateAPIView(LoginRequiredMixin, CreateAPIView):
    serializer_class = BioCreateSerializer

    def post(self, request, format=None):
        # serializer = UserCreateSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        try:
            user = User.objects.get(user=self.request)
        except:
            return Response(status=HTTP_400_BAD_REQUEST)
        address = Address.objects.create(street=request.data['street'],
                                         city=request.data['city'],
                                         country=request.data['country'],
                                         zip_code=request.data['zip_code'])

        emergency_contact = EmergencyContact.create(
            last_name=request.data['emergency_contact_last_name'],
            first_name=request.data['emergency_contact_first_name'],
            email=request.data['emergency_contact_email'],
            location=request.data['emergency_contact_location'],
            phone_number=request.data['emergency_contact_phone_number'])
        marital_status = MaritalStatus.objects.get(
            name=request.data['marital_status'])
        employment = Employment.objects.get(name=request.data['employment'])
        em_c_relationship = Relationship.objects.get(
            name=request.data['em_c_relationship'])
        gender = Sex.objects.get(name=request.data['sex'])
        id_type = IdentificationType.objects.get(name=request.data['id_type'])
        ethnicity = Ethnicity.objects.get(name=request.data['ethnicity'])
        blood_type = BloodType.objects.get(name=request.data['blood_type'])
        bio = Bio.objects.create(user=user,
                                 gender=request.data['gender'],
                                 notes=request.data['notes'],
                                 em_contact=emergency_contact,
                                 em_c_relationship=em_c_relationship,
                                 state=request.data['state'],
                                 main_id_type_no=request.data[
                                     'main_id_type_no'],
                                 address=address,
                                 birthday=request.data['birthday'],
                                 marital_status=marital_status,
                                 employment=employment,
                                 phone_number=request.data['phone_number'],
                                 id_type=id_type,
                                 ethnicity=ethnicity,
                                 blood_type=blood_type,
                                 preferred_language=request.data[
                                     'preferred_language'],
                                 religion=request.data['religion'])
        return Response(status=HTTP_201_CREATED)


class BioListAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = BioListSerializer
    queryset = Bio.objects.all()


class BioDetailAPIView(LoginRequiredMixin,
                       DestroyModelMixin,
                       UpdateModelMixin,
                       generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Bio.objects.get(pk=pk)
        except Bio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = BioDetailSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = BioDetailSerializer(
            bio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            bio = self.get_object(pk)
            bio.delete()
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

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
from django.contrib.auth import get_user_model
User = get_user_model()


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',

        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data


class GroupCreateSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GroupListSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GroupDetailSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class SexSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Sex
        fields = '__all__'


class MaritalStatusSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = MaritalStatus
        fields = '__all__'


class EmploymentSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Employment
        fields = '__all__'


class RelationshipSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Relationship
        fields = '__all__'


class EmergencyContactSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = EmergencyContact
        fields = '__all__'


class IdentificationTypeSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = IdentificationType
        fields = '__all__'


class AddressSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


class PhoneNumberSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = PhoneNumber
        fields = '__all__'


class BloodTypeSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = BloodType
        fields = '__all__'


class EthnicitySerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Ethnicity
        fields = '__all__'


class BioDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Bio
        fields = '__all__'


class BioCreateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Bio
        fields = '__all__'
        extra_kwargs = {"ssn":
                        {"write_only": True}
                        }

    def create(self, validated_data):
        return Patient.objects.create(**validated_data)


class BioListSerializer(ModelSerializer):

    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Bio
        fields = '__all__'

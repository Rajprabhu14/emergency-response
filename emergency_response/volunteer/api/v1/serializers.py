from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from common.validators import password_validator, phone_number_validator
from volunteer.models import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):

    uid = serializers.UUIDField(read_only=True)

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Volunteer.objects.all())])
    phone_number = serializers.CharField(
        max_length=13,
        required=True,
        validators=[UniqueValidator(queryset=Volunteer.objects.all()),
                    phone_number_validator
                    ]
    )
    password = serializers.CharField(max_length=16,
                                     min_length=8,
                                     required=True,
                                     write_only=True,
                                     validators=[password_validator])
    # testcase response hiding of password field
    conform_password = serializers.CharField(max_length=16,
                                             min_length=8,
                                             required=True,
                                             write_only=True,
                                             validators=[password_validator])
    is_volunteer = serializers.BooleanField(default=False, write_only=True)
    is_customer = serializers.BooleanField(default=False, write_only=True)
    # location = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['conform_password']:
            raise serializers.ValidationError(detail='Password not matching', code='Invalid Password')
        # validate input of is_customer, is_volunteer
        if validated_data['is_volunteer'] == validated_data['is_customer']:
            raise serializers.ValidationError(detail='Proxy Input', code='Proxy Input')
        return validated_data

    def create(self, validated_data):
        volunteer = Volunteer.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            location=validated_data['location'],
            password=validated_data['password'],
        )

        return volunteer

    class Meta:
        model = Volunteer
        multiple_lookup_field = ('uid', 'pk')
        fields = ['uid', 'email', 'name', 'phone_number', 'address',
                  'location', 'verfication_completed', 'other_details', 'password', 'conform_password','is_volunteer', 'is_customer']
        write_only_fields = ('location', 'password', 'conform_password')
        read_only_field = ('email', 'name', 'address', 'uid')


class ManipulateVolunteerSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=13,
        required=True,
        validators=[UniqueValidator(queryset=Volunteer.objects.all()),
                    phone_number_validator
                    ]
    )
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=500)
    other_details = serializers.CharField(max_length=500)
    verfication_completed = serializers.BooleanField(read_only=True)
    # latitude = serializers.FloatField(read_only=True)
    # longitude = serializers.FloatField(read_only=True)

    # def get_latitude(self):
    #     return 2.5

    # def get_longitude(self):
    #     return 2.5

    class Meta:
        model = Volunteer
        fields = ['uid', 'email', 'name', 'phone_number', 'address', 'verfication_completed', 'other_details']
        # write_only_fields = ('location', 'password', 'conform_password')
        # read_only_field = ('email', 'name', 'address', 'uid')


class UpdatePasswordVolunteerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16,
                                     min_length=8,
                                     required=True,
                                     write_only=True,
                                     validators=[password_validator])
    # testcase response hiding of password field
    conform_password = serializers.CharField(max_length=16,
                                             min_length=8,
                                             required=True,
                                             write_only=True,
                                             validators=[password_validator])

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['conform_password']:
            raise serializers.ValidationError(detail='Password not matching', code='Invalid Password')
        validated_data['password'] = make_password(validated_data['password'])
        return validated_data

    class Meta:
        model = Volunteer
        fields = ['uid', 'password', 'conform_password']

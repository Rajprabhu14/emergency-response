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
    location = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['conform_password']:
            raise serializers.ValidationError(detail='Password not matching', code='Invalid Password')
        return validated_data

    def create(self, validated_data):
        volunteer = Volunteer.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            location=validated_data['location'],
            password=validated_data['password'],
            # verfication_completed=validated_data['verfication_completed'],
            # other_details=validated_data['other_details'],
        )

        return volunteer

    class Meta:
        model = Volunteer
        multiple_lookup_field = ('uid', 'pk')
        fields = ['uid', 'email', 'name', 'phone_number', 'address',
                  'location', 'verfication_completed', 'other_details', 'password', 'conform_password']
        write_only_fields = ('location', 'password', 'conform_password')
        read_only_field = ('email', 'name', 'address', 'uid')

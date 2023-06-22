""" User Model Serializer """

# Django
from django.core.validators import RegexValidator
from django.contrib.auth import password_validation
from django.contrib.auth import authenticate

# Django Rest Framework
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from blog.users.models import User


class UserModelSerializer(ModelSerializer):
    """ User model serializer """

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')


class UserSignupSerializer(serializers.Serializer):
    """ User Sign Up Serializer"""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=2,
        max_length=12,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=16)
    password_confirmation = serializers.CharField(min_length=8, max_length=16)
    first_name = serializers.CharField(min_length=2, max_length=20)
    last_name = serializers.CharField(min_length=2, max_length=20)
    # Phone number
    phone_validator = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +111111111, up to 15 digits'
    )
    phone_number = serializers.CharField(
        validators=[phone_validator]
    )

    def validate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError("Passwords not match")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create(**data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        return instance

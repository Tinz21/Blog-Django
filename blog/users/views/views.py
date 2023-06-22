""" Users views """

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated)

# Serializers
from blog.users.serializers.users import (
    UserSignupSerializer,
    UserModelSerializer)

# Models
from blog.users.models import User


class UsersSignupView(APIView):
    """ Users Signup View """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class UsersApiView(APIView):
    """ Users API View

    Get and update users information
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        users = get_object_or_404(User, username=username)
        serializer = UserModelSerializer(users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSignupSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data=data, status=status.HTTP_202_ACCEPTED)

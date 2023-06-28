""" Public Posts Views """

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Models
from blog.posts.models.posts import PostsModel

# Serializers
from blog.posts.serializers.posts import PostsSerializer


class ViewPosts(viewsets.ViewSet):
    """ Posts Lists """

    permission_classes = [AllowAny]

    def list(self, request):
        instance = PostsModel.objects.filter(is_published=True, is_public=True)
        serializer = PostsSerializer(instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        instance = get_object_or_404(PostsModel, title=pk)
        if instance.is_public is False or instance.is_published is False:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = PostsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

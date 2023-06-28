""" Posts Views """

# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

# Models
from blog.posts.models.posts import PostsModel

# Serializers
from blog.posts.serializers.posts import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """ Posts Viewset """

    permission_classes = [permissions.AllowAny]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()

    def retrieve(self, request, pk):
        instance = get_object_or_404(PostsModel, title=pk)
        serializer = PostsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = get_object_or_404(PostsModel, title=pk)
        serializer = PostsSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(PostsModel, title=pk)
        instance.delete()
        return Response(data="deleted", status=status.HTTP_200_OK)

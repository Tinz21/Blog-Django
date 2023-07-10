""" Posts Views """

# Django REST Framework
from rest_framework import (viewsets,
                            permissions,
)

# Models
from blog.posts.models.posts import PostsModel

# Serializers
from blog.posts.serializers.posts import PostsSerializer
from blog.posts.permissions import IsOwner


class PostsViewSet(viewsets.ModelViewSet):
    """ Posts Viewset """

    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()
    lookup_field = 'title'

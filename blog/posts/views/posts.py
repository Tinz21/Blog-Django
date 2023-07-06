""" Posts Views """

# Django REST Framework
from rest_framework import viewsets
from rest_framework import permissions

# Models
from blog.posts.models.posts import PostsModel

# Serializers
from blog.posts.serializers.posts import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """ Posts Viewset """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()
    lookup_field = 'title'

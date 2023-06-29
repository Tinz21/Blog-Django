""" Comments views """

# Django Rest Framework
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

# Models
from blog.comments.models import Comment

# Serializers
from blog.comments.serializers import CommentsSerializer


class CommentsViewSet(ModelViewSet):
    """ Comments View Set """

    class_permission = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

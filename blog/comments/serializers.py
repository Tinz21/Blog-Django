""" Comments serializers """

# Django Rest Framework
from rest_framework import serializers

# Models
from blog.comments.models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    """ Comments Serializer """

    class Meta:
        model = Comment
        fields = ['name', 'content', 'post']

""" Posts Serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from blog.posts.models.posts import PostsModel


class PostsSerializer(serializers.ModelSerializer):
    """ Posts Serializer """

    class Meta:
        """ Meta class """

        model = PostsModel
        fields = ['title', 'content', 'is_public',
                  'is_published', 'publication_date',
                  'user']

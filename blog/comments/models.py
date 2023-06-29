""" Comments Models """

# Django
from django.db import models

# Utilities
from blog.utils.models import BaseModel


class Comment(BaseModel):
    """ Comments Model """

    content = models.CharField(max_length=500)
    name = models.CharField(max_length=25)
    post = models.ForeignKey(
        'posts.PostsModel',
        to_field='title',
        on_delete=models.CASCADE
    )

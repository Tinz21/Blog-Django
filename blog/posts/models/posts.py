""" Posts models """

# Django
from django.db import models

# utilities
from blog.utils.models import BaseModel


class PostsModel(BaseModel, models.Model):
    """ Posts Model """

    title = models.CharField(
        help_text="Post title",
        unique=True,
        max_length=50,
        null=False,
        blank=False
    )
    content = models.CharField(
        help_text="Post text",
        max_length=1500,
        null=False,
        blank=False
    )
    is_public = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    publication_date = models.DateTimeField(null=True)
    user = models.ForeignKey(
        'users.User',
        to_field='username',
        on_delete=models.SET_NULL,
        null=True
    )

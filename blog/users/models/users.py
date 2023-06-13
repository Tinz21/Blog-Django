""" Users Model """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator

# Utilities
from blog.utils.models import BaseModel


class User(BaseModel, AbstractUser, PermissionsMixin):
    """ User Model """

    email = models.EmailField(
        "Email Address",
        unique=True,
        error_messages={"unique": "User with that email already exist"},
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +111111111, up to 15 digits'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Clients are the main type of user'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the client have verified its email address'
    )

    def __str__(self):
        """ Return username """
        return self.username

    def get_short_name(self):
        """ Return username """
        return self.username
""" Django Models utilities """

# Django
from django.db import models


class BaseModel(models.Model):
    """ Common data models

    This model acts as an abstract base class from which every other models.
    Provides every table with de following attributes:
        + created (DateTime): Store the datetime the object was created
        + modified: (DateTime): Store the datetime the object was modified
    """

    created = models.DateTimeField(
        'Created at',
        auto_now_add=True,
        help_text="Object creation date"
    )
    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text="Object modification date"
    )

    class Meta:
        """ Meta option """

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

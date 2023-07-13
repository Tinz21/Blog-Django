""" Test Users.model """

# Django
from django.test import TestCase
from django.db import transaction

# Models
from blog.users.models.users import User


class TestModels(TestCase):
    """ Tests user Model """

    def setUp(self):
        self.user = User.objects.create(username="user_test",
                                        email='mail@mail.io',
                                        first_name="hola",
                                        phone_number="+54875698",
                                        )

    def test_model_attributes(self):
        with self.assertRaises(Exception) as context:
            with transaction.atomic():
                User(username="user_test").save()
        self.assertIn('username', str(context.exception))

        with self.assertRaises(Exception) as context:
            with transaction.atomic():
                User(username="user", email='mail@mail.io').save()
        self.assertIn('email', str(context.exception))

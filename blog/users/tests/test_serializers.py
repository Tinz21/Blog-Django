""" Test Users Serializer """

# Django
from django.test import TestCase

# Serializers
from blog.users.serializers.users import UserSignupSerializer

# Models
from blog.users.models.users import User


class TestSerializer(TestCase):
    """ Test Users Serializer """

    def setUp(self):
        self.user = User.objects.create(
            username="user_test", email='mail@mail.io',
            first_name="hola", last_name="zuzu",
            phone_number="+54875698", password="h1o2l3a4",
        )
        self.data_test = {
            "username": "user_tes", "first_name": "hola",
            "last_name": "zuzu", "email": 'mai@mail.io',
            "phone_number": "+566894812",
            "password": 'h1o2l3a4',
            "password_confirmation": 'h1o2l3a4'
        }
        self.user2 = UserSignupSerializer(data=self.data_test)

    def test_user_fields(self):
        self.user2.is_valid()
        errors = self.user2.errors
        fields = list(self.data_test.keys())
        for field in fields:
            self.assertNotIn(field, errors.keys())

    def test_passwords_validation(self):
        self.user2.is_valid()
        if self.user2.errors:
            with self.assertRaises(Exception) as context:
                self.user2.validate(data=self.data_test)
            self.assertIn('Passwords not match', str(context.exception))

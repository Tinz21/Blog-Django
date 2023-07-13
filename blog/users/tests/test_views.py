""" Test Users.Views """

# Django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Django REST Framework
from rest_framework.test import (APIClient,
                                 APIRequestFactory,
                                 force_authenticate
                                 )
# Models
from blog.users.models.users import User

# Views
from blog.users.views.views import UsersSignupView, UsersApiView


class TestSignup(TestCase):
    """ Test of user registration in the app """

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_user_signup(self):
        url = reverse('users:Signup')
        data = {
            "username": "user_test", "first_name": "Usersito",
            "last_name": "Usersito", "email": 'mail@mail.io',
            "phone_number": "+568794455", "password": 'h1o2l3a4',
            "password_confirmation": 'h1o2l3a4'
        }
        request = self.factory.post(url, data=data)
        view = UsersSignupView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)


class TestUsers(TestCase):
    """ Test the rest user app endpoints """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user_testing',  password='h1o2l3a4',
            email='test@mail.io'
        )
        self.factory = APIRequestFactory()
        self.view = UsersApiView.as_view()
        self.url = reverse('users:users', kwargs={
            'username': 'user_testing'
        })

    def test_user_login(self):
        client = APIClient()
        data = {
            'username': 'user_testing',
            'password': 'h1o2l3a4',
            'email': 'test@mail.io'
        }
        url = reverse('users:Login')
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    def test_user_get(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request, username='user_testing')
        self.assertEqual(response.status_code, 200)

    def test_user_update(self):
        user_updated = {
            "email": "test@mail.io", "username": "user_testing",
            "first_name": "client", "last_name": "client2",
            "phone_number": "+568975635", "password": "h1o2l3a4",
            "password_confirmation": "h1o2l3a4"
        }
        request = self.factory.put(self.url, data=user_updated)
        force_authenticate(request, user=self.user)
        response = self.view(request, username='user_testing')
        self.assertEqual(response.status_code, 202)

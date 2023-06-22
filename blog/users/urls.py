""" Urls Users """

# Django
from django.urls import path

# Django REST Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

# Views
from blog.users.views import UsersApiView, UsersSignupView


urlpatterns = [
    path('signup/', UsersSignupView.as_view(), name='Signup'),
    path('<username>', UsersApiView.as_view(), name='users'),
    path('login/', TokenObtainPairView.as_view(), name='Login'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


""" Project Urls """

# Django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('blog.users.urls', 'users'), namespace='signup')),
]

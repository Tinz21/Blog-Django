""" Project Urls """

# Django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('blog.users.urls', 'users'), namespace='users')),
    path('posts/', include(('blog.posts.urls', 'posts'), namespace='posts')),
    path('comments/', include(('blog.comments.urls', 'comments'), namespace='comments')),
]

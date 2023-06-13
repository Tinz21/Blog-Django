""" Users model admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from blog.users.models import User


class CustomUserAdmin(UserAdmin):
    """ User Model Admin """

    list_display = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)

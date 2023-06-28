""" Posts Model Admin """

# Django
from django.contrib import admin

# Models
from blog.posts.models.posts import PostsModel


class PostsAdmin(admin.ModelAdmin):
    """ Posts admin """

    list_display = ('title', 'content', 'is_published')
    list_filter = ('title', 'created', 'modified', 'publication_date')


admin.site.register(PostsModel, PostsAdmin)

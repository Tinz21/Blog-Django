""" Comments admin """

# Django
from django.contrib import admin

# Models
from blog.comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    """ Comments Admin """

    list_display = ('created', 'name', 'content', 'post')
    list_filter = ('created', 'name', 'post')


admin.site.register(Comment, CommentsAdmin)

from rest_framework.permissions import BasePermission
from blog.posts.models.posts import PostsModel


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['update', 'partial_update', 'destroy']:
            title = view.kwargs.get('title')
            try:
                instance = PostsModel.objects.get(title=title)
                user = instance.user
                return user == request.user.username
            except Exception:
                return False
        else:
            return True

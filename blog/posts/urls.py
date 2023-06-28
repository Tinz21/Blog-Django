""" Posts Urls """

# Django
from rest_framework.routers import DefaultRouter

# Views
from blog.posts.views import PostsViewSet, ViewPosts

router = DefaultRouter()

router.register(r'user', PostsViewSet, basename='posts')
router.register(r'public', ViewPosts, basename='view_posts')
urlpatterns = router.urls

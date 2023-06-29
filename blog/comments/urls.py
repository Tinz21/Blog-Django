""" Comments Urls """

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from blog.comments.views import CommentsViewSet


router = DefaultRouter()
router.register(r'', CommentsViewSet, basename='comments')
urlpatterns = router.urls

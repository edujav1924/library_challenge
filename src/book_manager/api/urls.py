from api.views.author import AuthorViewSet
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
urlpatterns = router.urls
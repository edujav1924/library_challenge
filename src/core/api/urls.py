from api.views.author import AuthorViewSet
from .views import BookViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')

book_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
book_router.register(r'authors', AuthorViewSet, basename='book-authors')

authors_router = routers.NestedSimpleRouter(
    router, r'authors', lookup='author')
authors_router.register(r'books', BookViewSet, basename='author-books')


urlpatterns = router.urls + book_router.urls + authors_router.urls

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

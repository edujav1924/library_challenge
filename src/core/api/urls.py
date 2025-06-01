"""
URL configuration for the core API.

This module sets up the routing for the API endpoints using Django REST Framework's routers,
including nested routers for handling relationships between books and authors.

Routers:
    - Uses DefaultRouter in DEBUG mode for browsable API, otherwise SimpleRouter.
    - Registers 'books' and 'authors' endpoints.
    - Sets up nested routes:
        - /books/{book_pk}/authors/ for authors of a specific book.
        - /authors/{author_pk}/books/ for books of a specific author.

Schema and Documentation:
    - /api/swagger/ provides Swagger UI for API documentation.
    - /api/redoc/ provides ReDoc UI for API documentation.

Dependencies:
    - Django settings for DEBUG flag.
    - Django REST Framework and drf-spectacular for API and schema views.
    - drf-nested-routers for nested resource routing.
"""

from django.conf import settings
from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import BookViewSet
from api.views.author import AuthorViewSet

router = None
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

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
         name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

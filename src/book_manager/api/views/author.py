from rest_framework import viewsets, permissions
from api.serializers.author import AuthorSerializer
from database.models import Author, Book
from api.serializers.book import BookSerializer
from rest_framework.pagination import PageNumberPagination


class AuthorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = []
    pagination_class = AuthorPagination

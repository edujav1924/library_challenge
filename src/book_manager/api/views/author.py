from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from database.models import Author
from api.serializers.author import AuthorSerializer


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

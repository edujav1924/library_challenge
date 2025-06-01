from django.db.models import Count
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from database.models import Book
from api.serializers.book import BookSerializer


class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.annotate(authors_count=Count('authors'))
    serializer_class = BookSerializer
    permission_classes = []
    pagination_class = BookPagination

    @action(detail=False, methods=['get'])
    def stats(self, request):
        data = Book.objects.aggregate(
            total_books=Count('id')
        )
        return Response(data)

from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from database.models import Book
from api.serializers.book import BookSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


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

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)

        # Filter books based on search query.
        # The search can be a title, author name, or publication year.
        # If the search is a digit, it will be treated as a publication year.
        if search:
            filters = Q(title__icontains=search) | Q(
                authors__name__icontains=search)
            if search.isdigit():
                filters = filters | Q(pub_year=search)
            queryset = queryset.filter(filters)
        return queryset

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name='search', description='Search for books by title, author name, or publication year.', required=False, type=str),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Override the list method to include authors_count in the response.
        """
        return super().list(request, *args, **kwargs)

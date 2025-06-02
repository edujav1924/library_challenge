from django.db.models import Count, Q
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from database.models import Book, Author
from api.serializers.book import BookSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
    ordering = 'title'  # Default ordering by title


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.annotate(num_authors=Count('authors'))
    serializer_class = BookSerializer
    permission_classes = []
    pagination_class = BookPagination

    @extend_schema(
        description="retireves statistics about books",
        summary="Get Book Statistics",
        tags=["books"],
        operation_id="get_book_stats",
        responses={200: OpenApiParameter(type=int, name="total_books", description="Total number of books")},
    )
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """ View to get statistics about books. """
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

        if ('author_pk' in self.kwargs):
            author_pk = self.kwargs['author_pk']
            queryset = queryset.filter(authors__id=author_pk).distinct()

        return queryset.order_by(self.pagination_class.ordering)

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name='search', description='Search for books by title, author name, or publication year.', required=False, type=str),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        # If 'author_pk' is provided, add the book to the author's books.
        if 'author_pk' in self.kwargs:
            author_pk = self.kwargs['author_pk']
            author_filter = Author.objects.filter(id=author_pk)

            if author_filter.exists():
                author = author_filter.first()
                author.books.add(serializer.instance)

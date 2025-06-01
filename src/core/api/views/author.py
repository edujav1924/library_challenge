from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from database.models import Author, Book
from api.serializers.author import AuthorSerializer


class AuthorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing author instances.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = []
    pagination_class = AuthorPagination

    def get_queryset(self):
        if 'book_pk' in self.kwargs:
            book_pk = self.kwargs['book_pk']
            return super().get_queryset().filter(books__id=book_pk).distinct()
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

        if 'book_pk' in self.kwargs:
            book_pk = self.kwargs['book_pk']
            book_filter = Book.objects.filter(id=book_pk)
            if book_filter.exists():
                book = book_filter.first()
                book.authors.add(serializer.instance)

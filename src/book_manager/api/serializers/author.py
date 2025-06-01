
from rest_framework import serializers
from database.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Author
        fields = (
            'id', 'name', 'nationality', 'birth_date',
            'created_at', 'updated_at', 'books_count'
        )
        ignore_fields = ['books_count']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_books_count(self, author):
        return author.books.count()
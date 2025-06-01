
from rest_framework import serializers
from database.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Author
        fields = (
            'id', 'name', 'nationality', 'birth_date',
            'created_at','books_count'
        )

    def get_books_count(self, author):
        return author.books.count()
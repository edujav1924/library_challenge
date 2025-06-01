
from rest_framework import serializers
from database.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    num_books = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = (
            'id', 'name', 'nationality', 'birth_date', 'num_books'
        )

    def get_num_books(self, author):
        return author.books.count()

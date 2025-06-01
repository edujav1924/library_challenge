
from rest_framework import serializers
from database.models import Book


class BookSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField(read_only=True)
    num_authors = serializers.IntegerField(read_only=True)
    class Meta:
        model = Book
        fields = (
            'id', 'title', 'description', 'pub_year', 'genre', 'author_names', 'num_authors'
        )

    def get_author_names(self, obj):
        return [author.name for author in obj.authors.all()]


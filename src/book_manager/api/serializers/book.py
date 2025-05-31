
from rest_framework import serializers
from database.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField(read_only=True)
    # authors_count = serializers.IntegerField(
    #    source='authors.count', read_only=True)
    authors_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Book
        fields = (
            'id', 'title', 'description', 'pub_year', 'genre',
            'created_at', 'updated_at', 'authors', 'author_names', 'authors_count'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_author_names(self, obj):
        return [author.name for author in obj.authors.all()]


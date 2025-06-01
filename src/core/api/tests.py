from django.test import TestCase
from database.models import Book, Author
from api.serializers.book import BookSerializer
from datetime import date
from api.serializers.author import AuthorSerializer
from rest_framework.test import APIClient


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Gabriel García Márquez", nationality="Colombian", birth_date=date(1927, 3, 6))
        self.book = Book.objects.create(
            title="Cien años de soledad",
            description="Una novela emblemática de la literatura latinoamericana.",
            pub_year=1967,
            genre="Realismo mágico"
        )
        self.book.authors.add(self.author)

    def test_book_serializer_fields(self):
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'pub_year',
                         'genre', 'author_names']))

    def test_book_serializer_content(self):
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        self.assertEqual(data['title'], "Cien años de soledad")
        self.assertEqual(
            data['description'], "Una novela emblemática de la literatura latinoamericana.")
        self.assertEqual(data['pub_year'], 1967)
        self.assertEqual(data['genre'], "Realismo mágico")

    def test_book_serializer_create(self):
        data = {
            'title': 'El amor en los tiempos del cólera',
            'description': 'Otra novela famosa.',
            'pub_year': 1985,
            'genre': 'Novela'
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        book = serializer.save()
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.genre, data['genre'])


class AuthorSerializerTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Gabriel García Márquez",
            nationality="Colombian",
            birth_date=date(1927, 3, 6)
        )

    def test_author_fields(self):
        serializer = AuthorSerializer(instance=self.author)
        data = serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['id', 'name', 'nationality',
                'birth_date', 'books_count'])
        )

    def test_author_content(self):
        serializer = AuthorSerializer(instance=self.author)
        data = serializer.data
        self.assertEqual(data['name'], "Gabriel García Márquez")
        self.assertEqual(data['nationality'], "Colombian")
        self.assertEqual(data['birth_date'], "1927-03-06")


class BookApiViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)
        self.assertTrue(isinstance(response.data['results'], list))

    def test_book_detail(self):
        book = Book.objects.create(
            title="Test Book",
            description="A book for testing.",
            pub_year=2023,
            genre="Fiction"
        )
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Test Book")
        self.assertEqual(response.data['pub_year'], 2023)

    def test_book_create_success(self):
        author = Author.objects.create(
            name="Test Author",
            nationality="Testlandian",
            birth_date="1980-01-01"
        )
        data = {
            "title": "New Book",
            "description": "A new book for testing.",
            "pub_year": 2024,
            "genre": "Test Genre"
        }
        response = self.client.post('/api/books/', data, format='json')
        assert response.status_code == 201
        assert Book.objects.filter(title="New Book").exists()
        book = Book.objects.get(title="New Book")
        assert book.genre == "Test Genre"

    def test_book_create_missing_fields(self):
        data = {
            "description": "Missing title and authors.",
            "pub_year": 2024,
            "genre": "Test Genre"
        }
        response = self.client.post('/api/books/', data, format='json')
        assert response.status_code == 400
        assert "title" in response.data

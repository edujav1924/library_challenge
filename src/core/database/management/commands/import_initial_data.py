# myapp/management/commands/import_initial_data.py

import datetime
import json
import os
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from database.models import Author, Book


class Command(BaseCommand):
    help = 'Imports initial data for the first time setup. Designed to be idempotent.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='author_and_books.json',
            help='Path to the JSON file containing author and book data. '
                 'Defaults to authors_and_books_records.json in the project\'s data/ directory.'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            'Starting initial data import...'))

        registers_count = Book.objects.count()
        if registers_count > 0:
            self.stdout.write(self.style.WARNING(
                'Data already exists in the database. This command is idempotent, '
                'so it will not overwrite existing data.'))
            return
        # Define the data you want to import
        # This could come from a CSV, JSON file, an API, etc.
        # For simplicity, we'll use a hardcoded list of dictionaries.

        json_file_name = options['file']
        project_root = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '../../../'))
        json_file_path = os.path.join(project_root, 'data', json_file_name)

        if not os.path.exists(json_file_path):
            raise CommandError(f'JSON file not found at: {json_file_path}')

        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                author_and_books_data = json.load(f)
                for row in author_and_books_data:
                    self._process_row(row)

            self.stdout.write(self.style.SUCCESS(
                'Initial data import completed successfully.'))
        except json.JSONDecodeError as e:
            raise CommandError(
                f'Error decoding JSON from {json_file_path}: {e}')
        except Exception as e:
            raise CommandError(f'Error reading file {json_file_path}: {e}')

    def _process_row(self, row):
        try:
            with transaction.atomic():
                # Create or get the author
                book, _ = Book.objects.get_or_create(
                    title=row['title'],
                    pub_year=row['publication_year'],
                    genre=row['genre'])

                authors_data = row.get('authors', [])
                for author_data in authors_data:
                    author, _ = Author.objects.get_or_create(
                        name=author_data['first_name'] +
                        ' ' + author_data['last_name'],
                        nationality=author_data['nationality'],
                        defaults={
                            'birth_date': datetime.datetime.strptime(author_data['birth_date'], '%Y-%m-%d').date(),
                        })
                    book.authors.add(author)
                book.save()
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Error processing row {row}: {e}'))

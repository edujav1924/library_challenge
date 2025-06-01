from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date',
                    'created_at', 'updated_at')
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_year',
                    'genre', 'created_at', 'updated_at')
    search_fields = ("title",)
    ordering = ("title",)
    filter_horizontal = ("authors",)
# Register your models here.

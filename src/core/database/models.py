from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the record was created")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="The date and time when the record was last updated")

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Author(BaseModel):
    name = models.CharField(max_length=255,
                            verbose_name="Name",
                            help_text="Enter the author's name",
                            null=False,
                            blank=False,
                            unique=True)
    nationality = models.CharField(max_length=100,
                                   verbose_name="Nationality",
                                   help_text="Enter the author's nationality",
                                   null=True,
                                   blank=True)

    birth_date = models.DateField(verbose_name="Birth Date",
                                  help_text="Enter the author's birth date",
                                  null=True,
                                  blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Create your models here.


class Book(BaseModel):
    title = models.CharField(max_length=255,
                             verbose_name="Title",
                             help_text="Enter the title of the book",
                             null=False,
                             blank=False,
                             unique=True)
    description = models.TextField(
        verbose_name="Description",
        help_text="Enter a brief description of the book",
        null=True,
        blank=True)
    pub_year = models.PositiveIntegerField(
        verbose_name="Publication Year",
        help_text="Enter the year the book was published",
        null=False,
        blank=False)
    genre = models.CharField(
        max_length=100,
        verbose_name="Genre",
        help_text="Enter the genre of the book",
        null=False,
        blank=False)
    authors = models.ManyToManyField(
        Author,
        related_name="books",
        verbose_name="Author",
        help_text="Select the author(s) of the book",
        blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title"]

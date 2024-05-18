from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return self.title
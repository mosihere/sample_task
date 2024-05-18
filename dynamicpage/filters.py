from django_filters.rest_framework import FilterSet
from .models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'published_date': ['lt', 'gt'],
            'author': ['exact']
        }
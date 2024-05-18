from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.filters import SearchFilter



class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    pagination_class = CustomPageNumberPagination
    search_fields = ['title']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'books']
    pagination_class = CustomPageNumberPagination
    search_fields = ['first_name', 'last_name']
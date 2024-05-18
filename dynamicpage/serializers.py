from .models import Author, Book
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    author = serializers.HyperlinkedRelatedField(view_name='dynamicpage:author-detail', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'author']


class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.HyperlinkedRelatedField(many=True, view_name='dynamicpage:book-detail', queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'books']
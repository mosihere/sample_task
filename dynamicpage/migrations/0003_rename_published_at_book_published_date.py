# Generated by Django 5.0.6 on 2024-05-18 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicpage', '0002_remove_author_books_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_at',
            new_name='published_date',
        ),
    ]

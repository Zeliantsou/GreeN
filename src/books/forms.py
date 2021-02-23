from django import forms
from . import models

# добавить fields после их определения в модели 'photo' 'publishing_year'   

class BookForm(models.ModelForm):
    class Meta:
        model = Book
        fields(
            'name',
            'price',
            'author',
            'series',
            'genre',
            'count_pages',
            'binding',
            'book_format',
            'isbn',
            'weight',
            'restriction',
            'publisher',
            'in_stock',
            'is_order',
            'rating',
            'created',
            'updated')
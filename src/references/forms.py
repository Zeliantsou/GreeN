from django import forms
from . import models

class BookAuthorForm(models.ModelForm):
    class Meta:
        model = BookAuthor
        fields = ('name', 'description')

class GenreForm(models.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')

class PublisherForm(models.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'description')

class SeriesForm(models.ModelForm):
    class Meta:
        model = Series
        fields = ('name', 'description')


# <!-- <li><a href="{% url 'author-detail' author.pk %}">{{ author.name }}</a></li></br> -->

# <!-- <li><a href="">{{ author.name }}</a></li></br> -->
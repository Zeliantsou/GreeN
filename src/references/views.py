from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from references.models import BookAuthor, Genre, Publisher, Series


<<<<<<< HEAD
def author_detail(request, pk):
    certain_author = BookAuthor.objects.get(pk=pk)
    name = certain_author.name
    description = certain_author.description
    context = {"name":name, "description":description}
    return render(request, template_name="author_detail.html", context=context)
    #
=======
class AllAuthors(ListView):
    model = BookAuthor
class AuthorDetail(DetailView):
    model = BookAuthor
class AuthorCreate(CreateView):
    model = BookAuthor
    success_url = '/author-list/'
    fields = ('name', 'description')
    # def get_absolute_url(self):
    #     return reverse_lazy('author-detail', kwargs={'pk': self.pk})
class AuthorUpdate(UpdateView):
    model = BookAuthor
    success_url = '/author-list/'
    fields = ('name', 'description')
class AuthorDelete(DeleteView):
    model = BookAuthor
    success_url = '/author-list/'


class AllGenres(ListView):
    model = Genre
class GenreDetail(DetailView):
    model = Genre
class GenreCreate(CreateView):
    model = Genre
    success_url = '/genre-list/'
    fields = ('name', 'description')
class GenreUpdate(UpdateView):
    model = Genre
    success_url = '/genre-list/'
    fields = ('name', 'description')
class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genre-list/'


class AllPublishers(ListView):
    model = Publisher
class PublisherDetail(DetailView):
    model = Publisher
class PublisherCreate(CreateView):
    model = Publisher
    success_url = '/publisher-list/'
    fields = ('name', 'description')
class PublisherUpdate(UpdateView):
    model = Publisher
    success_url = '/publisher-list/'
    fields = ('name', 'description')
class PublisherDelete(DeleteView):
    model = Publisher
    success_url = '/publisher-list/'


class AllSeries(ListView):
    model = Series
class SeriesDetail(DetailView):
    model = Series
class SeriesCreate(CreateView):
    model = Series
    success_url = '/series-list/'
    fields = ('name', 'description')
class SeriesUpdate(UpdateView):
    model = Series
    success_url = '/series-list/'
    fields = ('name', 'description')
class SeriesDelete(DeleteView):
    model = Series
    success_url = '/series-list/'


# Здесь было создано путем функций, но более локанично будет работать с классами,
# при это наследовавшись от импортированных классов.

# def all_authors(request):
#     all_book_authors = BookAuthor.objects.all()
#     context = {"all_book_authors":all_book_authors}
#     return render(request, template_name="all_book_authors.html", context=context)

# def author_detail(request, pk):
#     certain_author = BookAuthor.objects.get(pk=pk)
#     name = certain_author.name
#     description = certain_author.description
#     context = {"name":name, "description":description}
#     return render(request, template_name="author_detail.html", context=context)
>>>>>>> test_4_create_customer
    
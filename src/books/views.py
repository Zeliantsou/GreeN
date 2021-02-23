from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.models import Book

# Create your views here.  

class AllBooks(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    success_url = '/book-list/'
    fields = (
        'name',
        'description',
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
        'rating'
        )

class BookUpdate(UpdateView):
    model = Book
    success_url = '/book-list/'
    fields = (
        'name',
        'description',
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
        'rating'
        )

class BookDelete(DeleteView):
    model = Book
    success_url = '/book-list/'



# def promotion(request):
#     object_list = {}
#     massiv = []
#     item_max_pk = Book.objects.last()
#     max_pk = item_max_pk.pk
#     for i in range(5):
#         massiv.append(Book.objects.get(pk=max_pk))
#         max_pk = max_pk - 1
#     object_list["object_list"] = massiv
#     return render(request, template_name="books/book_list.html", context=object_list)


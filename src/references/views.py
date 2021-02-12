from django.shortcuts import render
from django.http import HttpResponse

from references.models import BookAuthor

def all_authors(request):
    all_book_authors = BookAuthor.objects.all()
    context = {"all_book_authors":all_book_authors}
    return render(request, template_name="all_book_authors.html", context=context)

def author_detail(request, pk):
    certain_author = BookAuthor.objects.get(pk=pk)
    name = certain_author.name
    description = certain_author.description
    context = {"name":name, "description":description}
    return render(request, template_name="author_detail.html", context=context)
    
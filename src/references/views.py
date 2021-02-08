from django.shortcuts import render
from django.http import HttpResponse

from references.models import BookAuthor

def home_page(request):
    the_first_author = BookAuthor.objects.first()
    context = {"first":the_first_author}
    return render(request, template_name="home.html", context=context)
    

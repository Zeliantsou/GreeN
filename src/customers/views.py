from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# также нужно будет импортировать все классы и функции, которыми будем здесь пользоваться

def home_customer(request):
    context = {}
    return render(request, template_name="home_customer.html", context=context)

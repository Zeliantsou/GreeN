from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib import messages

from customers.models import Customer
from customers.forms import UserRegisterForm

# Create your views here.



# # Создать класс для обработки домашней страницы
# # также нужно будет импортировать все классы и функции, которыми будем здесь пользоваться

def home_customer(request):
    context = {}
    return render(request, template_name="home_customer.html", context=context)

class CustomerList(ListView):
    model = Customer

class CustomerDetail(DetailView):
    model = Customer

def test_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, template_name="test_register.html", context={"form":form})
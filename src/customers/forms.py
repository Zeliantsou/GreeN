from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2')



# в класс CustomerForm добавить колонки 'group', 'home_address' после уточнения в модели

# class CustomerForm(madels.ModelForm):
#     class Meta:
#         model = Customer
#         fields = (
#             'login',
#             'password',
#             'email',
#             'name',
#             'surname',
#             'phone_number',
#             'country',
#             'city',
#             'index',
#             'first_address',
#             'second_address',
#             'extra')
#             #'group',
#             #'home_address')

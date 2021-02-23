from django.db import models


# Create your models here.

# class Customer(models.Model):



# если будут ссылки на другие классы, то on_delete PROTECT
# создание адреса. как лучше выполнить чтобы была отдельная таблица?
# есть ли специальный метод вместо CharField для записи телефонов???
# создание групп. к какой группе должно быть присвоение и как это сделать?
# есть поле emailField - исправить где емаил

class Customer(models.Model):
    login = models.CharField(
        max_length=20,
        verbose_name="customer's login")
    password = models.CharField(
        max_length=15,
        verbose_name="customer's password")
    email = models.CharField(
        max_length=30,
        verbose_name="customer's email")
    name = models.CharField(
        max_length=20,
        verbose_name="customer's name")
    surname = models.CharField(
        max_length=20,
        verbose_name="customer's surname")
    phone_number = models.CharField(
        max_length=20,
        verbose_name="customer's phone number")
    # group = models.CharField(
    #     max_length=20,
    #     verbose_name="customer's group")
    country = models.CharField(
        max_length=20,
        verbose_name="customer's country")
    city = models.CharField(
        max_length=20,
        verbose_name="customer's city")
    index = models.CharField(
        max_length=15,
        verbose_name="customer's index")
    first_address = models.CharField(
        max_length=30,
        verbose_name="customer's first address")
    second_address = models.CharField(
        max_length=30,
        verbose_name="customer's second address")
    # home_address = models.CharField(
    #     max_length=30,
    #     verbose_name="customer's home address") создать отдельный класс (таблицу) для адреса?
    extra = models.TextField(
        verbose_name="customer's extra information",
        null=True,
        blank=True)

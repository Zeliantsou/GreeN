from django.db import models
from books import models as books_models

# Create your models here.
# ссылка на имя покупателя, анонимный покупатель (как сделать)

class ItemInBasket(models.Model):
    # basket = models.ForeignKey(
    #     verbose_name = "wich basket")
    item_in_basket = models.ForeignKey(
        books_models.Book,
        verbose_name="wich item is in the basket",
        on_delete=models.PROTECT,
        related_name="item in basket +")
    count = models.PositiveSmallIntegerField(
        verbose_name="count of items")
    created = models.DateTimeField(
        verbose_name="created date time",
        auto_now=False,
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="updated date time",
        auto_now=True,
        auto_now_add=False)

class Basket(models.Model):
    #customer = models.ForeignKey()#
    item = models.ForeignKey(
        ItemInBasket,
        verbose_name="items",
        on_delete=models.PROTECT,
        related_name="basket")
    created = models.DateTimeField(
        verbose_name="created date time",
        auto_now = False,
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name="updated date time",
        auto_now=True,
        auto_now_add=False)
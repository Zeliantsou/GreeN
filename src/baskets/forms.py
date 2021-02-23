from django import forms
from . import models

# добавить поля после доработки модели

class BasketForm(models.ModelForm):
    class Meta:
        model = Basket
        fields = (
            'item',
            'created',
            'updated')

class ItemInBasketForm(models.ModelForm):
    class Meta:
        model = ItemInBasket
        fields = (
            'basket',
            'item_in_basket',
            'count',
            'created',
            'updated')
from django.contrib import admin

# Register your models here.

from . import models

class BasketAdmin(admin.ModelAdmin):
    # search_fields = ('<имя поля по которому искать>')
    list_display = [
        'item',
        'created',
        'updated',
    ]

class ItemInBasketAdmin(admin.ModelAdmin):
    # search_fields = ('<имя поля по которому искать>')
    list_display = [
        'item_in_basket',
        'count',
        'created',
        'updated',
    ]


admin.site.register(models.Basket, BasketAdmin)
admin.site.register(models.ItemInBasket, ItemInBasketAdmin)
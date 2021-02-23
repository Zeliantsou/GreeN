from django.contrib import admin

# Register your models here.

from . import models

class BookAdmin(admin.ModelAdmin):
    # search_fields = ('<имя поля по которому искать>')
    list_display = [
        'name',
        'price',
        #'author',
        'series',
        'genre'
    ]

admin.site.register(models.Book, BookAdmin)

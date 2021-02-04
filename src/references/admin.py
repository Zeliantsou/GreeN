from django.contrib import admin

# Register your models here.

from . import models

class BookAuthorAdmin(admin.ModelAdmin):
    # search_fields = ('<имя поля по которому искать>')
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]

class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]

admin.site.register(models.BookAuthor, BookAuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Series, PublisherAdmin)
admin.site.register(models.Publisher, SeriesAdmin)
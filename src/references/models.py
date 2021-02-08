from django.db import models

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Author's name",
        null=False, # по умолчанию всегда False, поэтому далее не указываем где будет False
        blank=False) # по умолчанию всегда False, поэтому далее не указываем где будет False
    description = models.TextField(
        verbose_name="Author description",
        null=True,
        blank=True)
    created = models.DateTimeField(
        verbose_name = "created date time",
        auto_now = False, # для фиксации последнего редактирования
        auto_now_add = True) # для фиксации создания записи
    updated = models.DateTimeField(
        verbose_name = "updated date time",
        auto_now = True, # для фиксации последнего редактирования
        auto_now_add = False) # для фиксации создания записи   
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Genre's name")
    description = models.TextField(
        verbose_name="Genre description",
        null=True,
        blank=True)
    created = models.DateTimeField(
        verbose_name = "created date time",
        auto_now = False,
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name = "updated date time",
        auto_now = True,
        auto_now_add = False) 
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Publisher's name")
    description = models.TextField(
        verbose_name="Publisher description",
        null=True,
        blank=True)
    created = models.DateTimeField(
        verbose_name = "created date time",
        auto_now = False,
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name = "updated date time",
        auto_now = True,
        auto_now_add = False)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Series name")
    description = models.TextField(
        verbose_name="Series description",
        null=True,
        blank=True)
    created = models.DateTimeField(
        verbose_name = "created date time",
        auto_now = False,
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name = "updated date time",
        auto_now = True,
        auto_now_add = False)
    def __str__(self):
        return self.name
#
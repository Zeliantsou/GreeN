from django.db import models
from references import models as ref_models

# Create your models here.
# создать поле для загрузки фото
# оствить только год в атрибуте года выпуска
# как сделать выпадающие списки
# формат для ISBN
# выпадающий список для ограничения возраста
# как организовать рейтинг  


class Book(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Book's name",
        null=False,
        blank=False)
    description = models.TextField(
        verbose_name="Book's description",
        null=True,
        blank=True)
    # photo = models.ImageField(
    #     upload_to='photos/%Y/%m/%d/', # создание пути хранения фото. Разбивает по папкам (по дате)
    #     verbose_name="Book's photo")
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Book's price")
    author = models.ManyToManyField(             #  ManyToManyField
        ref_models.BookAuthor,
        verbose_name="Book's author",
        # on_delete=models.PROTECT)
        related_name="books")
    series = models.ForeignKey(
        ref_models.Series,
        verbose_name="Book's series",
        on_delete=models.PROTECT,
        related_name="books")
    genre = models.ForeignKey(
        ref_models.Genre,
        verbose_name="Book's genre",
        on_delete=models.PROTECT,
        related_name="books")
    # publishing_year = models.DateField(
    #     verbose_name="the year of publishing")
    count_pages = models.PositiveIntegerField(
        verbose_name="Сount of pages")
    binding = models.CharField(
        max_length=50,
        verbose_name="Book's binding")
    book_format = models.CharField(
        max_length=20,
        verbose_name="Book's format")
    isbn = models.CharField(
        max_length=50,
        verbose_name="Book's ISBN")
    weight = models.PositiveIntegerField(
        verbose_name="Book's weight")
    restriction = models.CharField(
        max_length=20,
        verbose_name="Book's restriction")
    publisher = models.ForeignKey(
        ref_models.Publisher,
        verbose_name="Book's publisher",
        on_delete=models.PROTECT,
        related_name="books")
    in_stock = models.PositiveIntegerField(
        verbose_name="Count in stock")
    is_order = models.BooleanField(
        verbose_name="Possibility of order",
        default=True)
    rating = models.PositiveIntegerField(
        verbose_name="Book's rating")
    created = models.DateTimeField(
        verbose_name = "created date time",
        auto_now = False,
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name = "updated date time",
        auto_now = True,
        auto_now_add = False)
        
        

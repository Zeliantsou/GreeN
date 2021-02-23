# Generated by Django 3.1.6 on 2021-02-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0003_auto_20210204_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name="Book's name")),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Book's price")),
                ('count_pages', models.PositiveIntegerField(verbose_name='Сount of pages')),
                ('binding', models.CharField(max_length=50, verbose_name="Book's binding")),
                ('book_format', models.CharField(max_length=20, verbose_name="Book's format")),
                ('isbn', models.CharField(max_length=50, verbose_name="Book's ISBN")),
                ('weight', models.PositiveIntegerField(verbose_name="Book's weight")),
                ('restriction', models.CharField(max_length=20, verbose_name="Book's restriction")),
                ('in_stock', models.PositiveIntegerField(verbose_name='Count in stock')),
                ('is_order', models.BooleanField(default=True, verbose_name='Possibility of order')),
                ('rating', models.PositiveIntegerField(verbose_name="Book's rating")),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated date time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.bookauthor', verbose_name="Book's author")),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.genre', verbose_name="Book's genre")),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.publisher', verbose_name="Book's publisher")),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.series', verbose_name="Book's series")),
            ],
        ),
    ]

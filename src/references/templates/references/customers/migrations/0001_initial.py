# Generated by Django 3.1.6 on 2021-02-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name="customer's login")),
                ('password', models.CharField(max_length=15, verbose_name="customer's password")),
                ('email', models.CharField(max_length=30, verbose_name="customer's email")),
                ('name', models.CharField(max_length=20, verbose_name="customer's name")),
                ('surname', models.CharField(max_length=20, verbose_name="customer's surname")),
                ('phone_number', models.CharField(max_length=20, verbose_name="customer's phone number")),
                ('country', models.CharField(max_length=20, verbose_name="customer's country")),
                ('city', models.CharField(max_length=20, verbose_name="customer's city")),
                ('index', models.CharField(max_length=15, verbose_name="customer's index")),
                ('first_address', models.CharField(max_length=30, verbose_name="customer's first address")),
                ('second_address', models.CharField(max_length=30, verbose_name="customer's second address")),
                ('extra', models.TextField(blank=True, null=True, verbose_name="customer's extra information")),
            ],
        ),
    ]

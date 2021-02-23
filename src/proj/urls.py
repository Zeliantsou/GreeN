"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from references import views as ref_views
from customers import views as cust_views
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cust_views.promotion, name='home-customer'), # предусмотреть вывод страницы классом
# ---------------------------------------------------------------------------------------------------
    path('author-list/', ref_views.AllAuthors.as_view(), name='author-list'),
    path('author-list/<int:pk>/', ref_views.AuthorDetail.as_view(), name='author-detail'),
    path('author-create', ref_views.AuthorCreate.as_view(), name='author-create'),
    path('author-update/<int:pk>/', ref_views.AuthorUpdate.as_view(), name='author-update'),
    path('author-delete/<int:pk>/', ref_views.AuthorDelete.as_view(), name='author-delete'), 
# ---------------------------------------------------------------------------------------------------
    path('genre-list/', ref_views.AllGenres.as_view(), name='genre-list'),
    path('genre-list/<int:pk>/', ref_views.GenreDetail.as_view(), name='genre-detail'),
    path('genre-create', ref_views.GenreCreate.as_view(), name='genre-create'),
    path('genre-update/<int:pk>/', ref_views.GenreUpdate.as_view(), name='genre-update'),
    path('genre-delete/<int:pk>/', ref_views.GenreDelete.as_view(), name='genre-delete'),
# ---------------------------------------------------------------------------------------------------
    path('publisher-list/', ref_views.AllPublishers.as_view(), name='publisher-list'),
    path('publisher-list/<int:pk>/', ref_views.PublisherDetail.as_view(), name='publisher-detail'),
    path('publisher-create', ref_views.PublisherCreate.as_view(), name='publisher-create'),
    path('publisher-update/<int:pk>/', ref_views.PublisherUpdate.as_view(), name='publisher-update'),
    path('publisher-delete/<int:pk>/', ref_views.PublisherDelete.as_view(), name='publisher-delete'),
# ---------------------------------------------------------------------------------------------------
    path('series-list/', ref_views.AllSeries.as_view(), name='series-list'),
    path('series-list/<int:pk>/', ref_views.SeriesDetail.as_view(), name='series-detail'),
    path('series-create', ref_views.SeriesCreate.as_view(), name='series-create'),
    path('series-update/<int:pk>/', ref_views.SeriesUpdate.as_view(), name='series-update'),
    path('series-delete/<int:pk>/', ref_views.SeriesDelete.as_view(), name='series-delete'),
# ---------------------------------------------------------------------------------------------------
    path('book-list/', books_views.AllBooks.as_view(), name='book-list'),
    path('book-list/<int:pk>/', books_views.BookDetail.as_view(), name='book-detail'),
    path('book-create', books_views.BookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>/', books_views.BookUpdate.as_view(), name='book-update'), 
    path('book-delete/<int:pk>/', books_views.BookDelete.as_view(), name='book-delete'),
# ---------------------------------------------------------------------------------------------------
    path('customer-registration/', cust_views.test_register, name='customer-registration') # тестирование регистрации
    
]
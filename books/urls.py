from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_new, name='book_new'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path('authors/', views.author_list, name='author_list'),
    path('authors/new/', views.author_new, name='author_new'),
    path('authors/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    path('aggregation_methods/', views.aggregation, name='aggregate'),
    path('total_books/', views.total_books, name='total_books'),
    path('average_price/', views.average_price, name='average_price'),
    path('oldest_newest_books/', views.oldest_and_newest_books, name='oldest_newest_books'),
    path('books_published_each_year/', views.books_published_each_year, name='books_published_each_year'),
]
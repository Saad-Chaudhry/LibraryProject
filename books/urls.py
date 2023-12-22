from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.RegisterPageView.as_view(), name='register'),

    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/new/', views.BookNewView.as_view(), name='book_new'),
    path('books/<int:pk>/edit/', views.BookEditView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/new/', views.AuthorNewView.as_view(), name='author_new'),
    path('authors/<int:pk>/edit/', views.AuthorEditView.as_view(), name='author_edit'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),

    path('aggregation_methods/', views.AggregationView.as_view(), name='aggregate'),
    path('total_books/', views.TotalBooksView.as_view(), name='total_books'),
    path('average_price/', views.AveragePriceView.as_view(), name='average_price'),
    path('oldest_newest_books/', views.OldestAndNewestBooksView.as_view(), name='oldest_newest_books'),
    path('books_published_each_year/', views.BooksPublishedEachYearView.as_view(), name='books_published_each_year'),
]
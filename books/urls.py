from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.RegisterPageView.as_view(), name='register'),

    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/new/', views.BookNewView.as_view(), name='book_new'),
    path('books/edit/<int:pk>/', views.BookEditView.as_view(), name='book_edit'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),

    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/new/', views.AuthorNewView.as_view(), name='author_new'),
    path('authors/edit/<int:pk>/', views.AuthorEditView.as_view(), name='author_edit'),
    path('authors/delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='author_delete'),

    path('aggregation_methods/', views.AggregationView.as_view(), name='aggregate'),
]
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Author, Book

admin.site.register(User, UserAdmin)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_year', 'isbn', 'price')

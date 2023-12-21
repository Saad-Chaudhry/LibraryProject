from django.forms import ModelForm
from .models import User, Book, Author
from django import forms
from django.contrib.auth.forms import UserCreationForm

class myUserCreationForm(UserCreationForm):
    password2 = forms.CharField(label='Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
        },

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn', 'price']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'address']

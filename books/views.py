from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import logout
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.db.models import Q
from .models import Book, Author
from .forms import myUserCreationForm, BookForm, AuthorForm, LoginForm
from django.views.generic import FormView, ListView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "books/home.html"

class LoginPageView(LoginView):
    template_name='books/login.html'
    authentication_form = LoginForm

class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')

class RegisterPageView(FormView):
    template_name = 'books/signup.html'
    form_class = myUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, 'An error occurred during registration.')
        return self.render_to_response(self.get_context_data(form=form))

class BookListView(LoginRequiredMixin, ListView):
    model = Book

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return self.model.objects.filter(Q(title__icontains=q))

class AuthorListView(LoginRequiredMixin, ListView):
    model = Author

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            names = q.split()
            if len(names) == 1:
                first_name = last_name = names[0]
            elif len(names) >= 2:
                first_name = names[0]
                last_name = ' '.join(names[1:])
            else:
                authors = self.model.objects.none()

            authors = self.model.objects.filter(
                Q(first_name__icontains=first_name) |
                Q(last_name__icontains=last_name)
            )
        else:
            authors = self.model.objects.all()
        return authors

class BookNewView(LoginRequiredMixin, FormView):
    template_name = 'books/book_add.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BookEditView(LoginRequiredMixin, UpdateView):
    template_name = 'books/book_edit.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'

class AuthorNewView(LoginRequiredMixin, FormView):
    template_name = 'books/author_add.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AuthorEditView(LoginRequiredMixin, UpdateView):
    template_name = 'books/author_edit.html'
    model = Author
    form_class = AuthorForm
    success_url = '/authors/'

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/authors/'

class AggregationView(LoginRequiredMixin, View):

    def get(self, request):
        total_books_count = Book.objects.count()
        average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
        oldest_book = Book.objects.order_by('publication_year').first()
        newest_book = Book.objects.order_by('-publication_year').first()
        books_per_year = Book.objects.values('publication_year').annotate(count=Count('id')).order_by('publication_year')
        response_content = []
        for year in books_per_year:
            response_content.append(f'Published Year: {year["publication_year"]}, Books: {year["count"]}')
        context = {
            'total_books_count': total_books_count,
            'average_price': average_price,
            'oldest_book': oldest_book,
            'newest_book': newest_book,
            'response_content': response_content,
            }
        return render(request, 'books/aggregation_methods.html', context)

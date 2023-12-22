from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.db.models import Q
from .models import Book, Author
from .forms import myUserCreationForm, BookForm, AuthorForm, LoginForm
from django.views.generic import FormView, ListView, TemplateView, UpdateView
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

class BookDeleteView(LoginRequiredMixin, View):
    def get(self, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect('book_list')

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

class AuthorDeleteView(LoginRequiredMixin, View):
    def get(self, pk):
        author = Author.objects.get(id=pk)
        author.delete()
        return redirect('author_list')

class AggregationView(LoginRequiredMixin, TemplateView):
    template_name = 'books/aggregation_methods.html'

class TotalBooksView(LoginRequiredMixin, View):
    def get(self, request):
        total_books_count = Book.objects.count()
        return HttpResponse(f'Total Number of Books: {total_books_count}')

class AveragePriceView(LoginRequiredMixin, View):
    def get(self, request):
        average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
        return HttpResponse(f'Average Price of Books: {average_price}')

class OldestAndNewestBooksView(LoginRequiredMixin, View):
    def get(self, request):
        oldest_book = Book.objects.order_by('publication_year').first()
        newest_book = Book.objects.order_by('-publication_year').first()
        return HttpResponse(f'Oldest Book: {oldest_book.title} ({oldest_book.publication_year}) <---'
                        f'---> Newest Book: {newest_book.title} ({newest_book.publication_year})')

class BooksPublishedEachYearView(LoginRequiredMixin, View):
    def get(self, request):
        books_per_year = Book.objects.values('publication_year').annotate(count=Count('id')).order_by('publication_year')
        response_content = 'Books Published Each Year:\n'
        for year in books_per_year:
            response_content += f'[{year["publication_year"]}: {year["count"]} books] <--->\n'
        return HttpResponse(response_content)

from django.shortcuts import render, redirect
from .models import User, Book, Author
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import myUserCreationForm, BookForm, AuthorForm
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.db.models import Q

def home(request):
    return render(request, 'books/home.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try :
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit') 
    return render(request, 'books/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = myUserCreationForm()
    if request.method == 'POST':
        form = myUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    context={'form': form}
    return render(request, 'books/signup.html', context)

def book_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = Book.objects.filter(
        Q(title__icontains=q)
        )
    return render(request, 'books/books_list.html', {'books': books})

def author_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q:
        names = q.split()
        if len(names) == 1:
            first_name = last_name = names[0]
        elif len(names) >= 2:
            first_name = names[0]
            last_name = ' '.join(names[1:])
        else:
            authors = Author.objects.none()

        authors = Author.objects.filter(
            Q(first_name__icontains=first_name) |
            Q(last_name__icontains=last_name)
        )
    else:
        authors = Author.objects.all()
    return render(request, 'books/authors_list.html', {'authors': authors})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_add.html', {'form': form})

def book_edit(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book_list')

def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'books/author_add.html', {'form': form})

def author_edit(request, pk):
    author = Author.objects.get(id=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/author_edit.html', {'form': form})

def author_delete(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('author_list')

def aggregation(request):
    return render(request, 'books/aggregation_methods.html')

def total_books(request):
    total_books_count = Book.objects.count()
    return HttpResponse(f'Total Number of Books: {total_books_count}')

def average_price(request):
    average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
    return HttpResponse(f'Average Price of Books: {average_price}')

def oldest_and_newest_books(request):
    oldest_book = Book.objects.order_by('publication_year').first()
    newest_book = Book.objects.order_by('-publication_year').first()
    return HttpResponse(f'Oldest Book: {oldest_book.title} ({oldest_book.publication_year}) <---'
                        f'---> Newest Book: {newest_book.title} ({newest_book.publication_year})')

def books_published_each_year(request):
    books_per_year = Book.objects.values('publication_year').annotate(count=Count('id')).order_by('publication_year')
    response_content = 'Books Published Each Year:\n'
    for year in books_per_year:
        response_content += f'[{year["publication_year"]}: {year["count"]} books] <--->\n'
    return HttpResponse(response_content)

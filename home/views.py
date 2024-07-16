from django.shortcuts import render, redirect
from home.forms import BookForm, Userregistration
from home.models import Book, DownloadCount
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def Home(request):

    return render(request, 'home.html')

def Explore(request):

    return render(request, 'explore.html')

def UserBooks(request):
    user_books = Book.objects.filter(uploaded_by=request.user)
    context = {
        'books':user_books
    }

@login_required
def book_upload(request):
    books = Book.objects.all
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.save()
            DownloadCount.objects.create(book=book)

            return redirect('create')
        
    else:
        form = BookForm()
    
    user_books = Book.objects.filter(uploaded_by=request.user)
    book_stats = {book.id: DownloadCount.objects.create(book=book).download_count for book in user_books}
    return render(request, 'create.html', {'form':form, 'user_books':user_books, 'book_stats':book_stats, 'books':books})

def Explore(request):
    books= Book.objects.all()

    return render(request, 'explore.html', {'books': books})

@login_required
def delete(request, id):
    books = get_object_or_404(Book, id=id)
    books.delete()
    return redirect('create')

def my_books(request):

    books = Book.objects.all()

def register(request):
    if request.method == 'POST':
        form = Userregistration(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('create')
    else:
        form = Userregistration()
    return render(request, 'registration/register.html', {'form':form})

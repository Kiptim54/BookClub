from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .request import search_books
from .forms import ProfileForm

# Create your views here.
def landing_page(request):
    title="Book Club | Home"

    return render(request, 'views/index.html', {"title":title})

def books_page(request):
    title="Book Club | Book Suggestions"
    book_searched=search_books('chicklit')
    

    return render(request, 'api/books.html', {"books":book_searched})

def search_book(request):
    title="Book Results"
    if 'searchbook' in request.GET and request.GET['searchbook']:
        search_term=request.GET.get('searchbook')
        book_searched=search_books(search_term)
        

    return render(request, 'api/searched_book.html', {"books":book_searched})

def create_profile(request):
    title="Book Club | Profile"
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.user=current_user
            form.save()
            return redirect('landing_page')
    else:
        form=ProfileForm()
    return render(request, 'forms/profile.html', {"title":title, "form":form})
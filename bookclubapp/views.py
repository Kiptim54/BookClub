from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .request import search_books

# Create your views here.

def landing_page(request):
    title="Book Club | Home page"
    book_searched=search_books('chicklit')
    

    return render(request, 'api/index.html', {"books":book_searched})

def search_book(request):
    title="Book Results"
    if 'searchbook' in request.GET and request.GET['searchbook']:
        search_term=request.GET.get('searchbook')
        book_searched=search_books(search_term)
        

    return render(request, 'api/searched_book.html', {"books":book_searched})
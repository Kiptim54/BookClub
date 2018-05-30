from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .request import search_books

# Create your views here.

def landing_page(request):
    book_searched=search_books('purple')
    print(book_searched)

    return render(request, 'index.html', {"books":book_searched})
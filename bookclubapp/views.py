from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .models import Book
from .request import search_books
from .forms import ProfileForm, GroupForm, CommentForm, ReviewForm, BookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


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
        

    return render(request, 'api/searched_book.html', {"books":book_searched, "title":title})

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


def create_group(request):
    title="Book Club | Create Group"
    current_user=request.user
    if request.method=='POST':
        form=GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.Group_owner=current_user
            form.save()

    else:
        form=GroupForm()
    return render(request, 'forms/group.html',{"form":form, "title":title})



def sign_up(request):
    title="Book Club | Sign Up"
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landing_page')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html', {"form":form, "title":title})



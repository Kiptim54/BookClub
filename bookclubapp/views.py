from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
from .models import Book
from .request import search_books
from .forms import ProfileForm, GroupForm, CommentForm, ReviewForm, BookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Books,Comment,Review,Groups, Question
from datetime import datetime
import random


def landing_page(request):
    title="Book Club | Home"

    return render(request, 'views/index.html', {"title":title})

def books_page(request):
    title="Book Club | Book Suggestions"
    try:
        book_searched=search_books('chicklit')
        return render(request, 'api/books.html', {"books":book_searched, "title":title})
    except:
        error="Sorry you seem to be having an internet connection problem.Try again"

    return render(request, 'api/books.html', {"title":title, "error":error})



def search_book(request):
    title="Book Results"
    # try:
    search_term = request.GET.get('searchbook')
    book_searched = search_books(search_term)

    if 'searchbook' in request.GET and request.GET['searchbook']:
        search_term=request.GET.get('searchbook')
        book_searched = search_books(search_term)
    return JsonResponse(book_searched, safe=False)
    
    

def single_review(request, id):
    current_user=request.user.username
    title="BookClub | Review"
    review=get_object_or_404(Review,id=id)
    comments=Comment.objects.filter(review=review)
    print(review)
    form=CommentForm()
    return render(request, 'views/single_review.html',{"review":review, "form":form,"title":title, "comments":comments})

def comment(request, id):
    current_user=request.user
    date = datetime
    print(date)
    profile=Profile.objects.get(user=current_user)
    name=profile.name
    print(profile)
    review=get_object_or_404(Review,id=id)
    comment = request.POST['comment']
    if request.method=='POST':
        saved=Comment.objects.create(comment=comment, user=current_user, review=review, time_posted=date)
        print(saved)
        print(model_to_dict(saved))

    return JsonResponse(model_to_dict(saved))
 



def display_reviews(request):
    title="Book Club | Review"
    reviews=Review.objects.all()
    current_user=request.user
    return render(request, 'views/reviews.html', {"reviews":reviews,"title":title})


def create_profile(request):
    title="Book Club | Profile"
    current_user=request.user
    current_user.id=request.user.id
    print(current_user)
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=current_user
            profile.save()
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
            group=form.save(commit=False)
            group.Group_owner=current_user
            group.save()
            return redirect('landing_page')
    else:
        form=GroupForm()
    return render(request, 'forms/group.html',{"form":form, "title":title})


def create_book(request):
    title="Book Club | Book"
    current_user=request.user
    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)
        if form.is_valid():
            book=form.save(commit=False)
            book.save()
            return redirect('landing_page')
    else:
        form=BookForm()
    return render(request, 'forms/book.html', {"title":title, "form":form})


# def create_comment(request):

#     title='Book Club | Comment'
#     current_user=request.user
#     if request.method=='POST':
#         form=CommentForm(request.POST, request.FILES)
#         comment=form.save(commit=False)
#         comment.user=current_user
#         comment.save()
#         return redirect('landing_page')
#     else:
#         form=CommentForm()
#     return render(request, 'forms/comment.html', {"form":form,"title":title})

def write_review(request):
    title='Book Club | Review'
    current_user=request.user
    if request.method=='POST':
        form=ReviewForm(request.POST, request.FILES)
        review=form.save(commit=False)
        review.user=current_user
        review.save()
        return redirect('landing_page')
    else:
        form=ReviewForm()
    return render(request, 'forms/review.html', {"form":form,"title":title})




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


def get_question(request):
    questions=Question.objects.all()
    chosen=random.choice(questions)
    print(chosen)
    print(questions)
    return JsonResponse(model_to_dict(chosen), safe=False)
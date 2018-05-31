from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('books/', views.books_page, name='books_page' ),
    path('search/', views.search_book, name='search_book'),
    path('profile/edit/', views.create_profile, name='create_profile'),
    path('group/edit', views.create_group, name='create_group'),
    path('signup/', views.sign_up, name='sign_up'),
]

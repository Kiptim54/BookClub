from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('books/', views.books_page, name='books_page' ),
    path('search/', views.search_book, name='search_book'),
    path('profile/edit/', views.create_profile, name='create_profile'),
    path('group/edit', views.create_group, name='create_group'),
    path('book/edit', views.create_book, name='create_book'),
    path('signup/', views.sign_up, name='sign_up'),
    path('review/', views.write_review, name='write_review'),
    path('review/<int:id>', views.single_review, name='single_review'),
    path('reviews/', views.display_reviews, name='display_reviews'),
    path('review/ajax/comment/<int:id>', views.comment, name='comment'),
    path('ajax/questions', views.get_question, name='question'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
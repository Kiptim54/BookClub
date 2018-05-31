import urllib.request, json
from .models import Book

api_key='AIzaSyBq3oH1P0mDfWT5y1tzvnUbZIoUwFzU0ZM'
base_url='https://www.googleapis.com/books/v1/volumes?q={}&key={}'

def search_books(search_item):
    book_results_url=base_url.format(search_item,api_key)
    print(book_results_url)

    with urllib.request.urlopen(book_results_url)as url:
        get_books_data=url.read()
        get_books_response=json.loads(get_books_data)

        book_results=None

        if get_books_response['items']:
            book_results=get_books_response['items']
            return book_results
        else:
            pass

      



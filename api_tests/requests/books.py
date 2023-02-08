import requests

def get_books(limit='', book_type=''):
    return requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}&type={book_type}")

def get_book(id):
    return requests.get(f"https://simple-books-api.glitch.me/books/{id}")
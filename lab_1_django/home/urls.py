from django.urls import path
from .views import index, store_books, book_details, delete_book, create_book, update_book

app_name = 'books'

urlpatterns = [
    path('', index, name='home-index'),
    path('allbooks/', store_books, name='home-books'),
    path('book_details/<int:id>', book_details, name='book-details'),
    path('delete_book/<int:id>', delete_book, name='delete-book'),
    path('delete_book/<int:id>', delete_book, name='delete-book'),
    path('create/', create_book, name='create-book'),
    path('update/<int:book_id>', update_book, name='update-book'),

]
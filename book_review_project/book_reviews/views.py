from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_reviews/book_list.html'
    context_object_name = 'books'
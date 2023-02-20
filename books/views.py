from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from .models import Book

class BookListPageView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'
    
class bookListDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')


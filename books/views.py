from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Book, BookCategory
from django.urls import reverse_lazy
from django.db.models import Sum

# BOOK CRUD VIEWS --
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

# CATEGORY CRUD VIEWS --
class CategoryListView(ListView):
    model = BookCategory
    template_name = 'books/category_list.html'

class CategoryCreateView(CreateView):
    model = BookCategory
    fields = '__all__'
    template_name = 'books/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = BookCategory
    fields = '__all__'
    template_name = 'books/category_form.html'
    success_url = reverse_lazy('category-list')

# EXPENSE REPORT VIEW
def expense_report(request):
    data = (
        BookCategory.objects
        .annotate(total_expenses=Sum('book__distribution_expenses'))
        .values('name', 'total_expenses')
    )
    categories = [entry['name'] for entry in data]
    expenses = [entry['total_expenses'] or 0 for entry in data]
    return render(request, 'books/report.html', {
        'categories': categories,
        'expenses': expenses,
    })

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum

def expense_report(request):
    data = (
        BookCategory.objects
        .annotate(total_expenses=Sum('book__distribution_expenses'))
        .values('name', 'total_expenses')
    )
    categories = [entry['name'] for entry in data]
    expenses = [entry['total_expenses'] or 0 for entry in data]
    return render(request, 'books/report.html', {
        'categories': categories,
        'expenses': expenses,
    })


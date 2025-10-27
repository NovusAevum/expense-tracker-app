from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),

    path('report/', views.expense_report, name='expense-report'),
]

path('report/pdf/', views.export_report_pdf, name='report-pdf'),
path('report/excel/', views.export_report_excel, name='report-excel'),

from .api import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/books', BookViewSet)

urlpatterns += router.urls


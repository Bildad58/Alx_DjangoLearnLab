# from django.contrib.auth import urls
from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView


urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name= 'books/detail'),
    path('createbook/', BookCreateView.as_view(), name = 'books/create'),
    path('books/', BookListView.as_view(), name = 'books/list'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name = 'books/update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name = 'books/delete'),


]
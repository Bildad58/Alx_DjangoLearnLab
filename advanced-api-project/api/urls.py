# from django.contrib.auth import urls
from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView


urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name= 'book-detail'),
    path('createbook/', BookCreateView.as_view(), name = 'book-create'),
    path('books/', BookListView.as_view(), name = 'book-list'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name = 'book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name = 'book-delete'),


]
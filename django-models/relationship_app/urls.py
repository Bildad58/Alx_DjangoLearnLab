from django.urls import path
from .views import list_books, LibraryDetailView
from .import views

urlpatterns = [
    # path('books/', list_books, name='list_books.html'),
    # path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]



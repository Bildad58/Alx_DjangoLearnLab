
from .import views
from django.contrib.auth import views as auth_views

from .views import list_books
from django.urls import path
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

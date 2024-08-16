from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


def list_books(request):
      books = Book.objects.all()  # Fetch all book instances from the database
      return render(request, 'relationship_app/list_books.html', {'books': books})
    
  

  
def LibraryDetailView(self, request):
    """Injects additional context data specific to the book."""
    context = {'detail_view': book}
    book = self.get_object()# Retrieve the current book instance
    return render(request, 'relationship_app/library_detail.html', context)
    
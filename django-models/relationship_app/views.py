from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# from django.http import HttpResponse

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)
      # return HttpResponse(book_list, content_type="text/plain")
  
# class DetailView(DetailView):
#   """A class-based view for displaying details of a specific book."""
  
def LibraryDetailView(self, request):
    """Injects additional context data specific to the book."""
    # context = super().get_context_data(**kwargs)  # Get default context data
    context = {'detail_view': book}
    book = self.get_object()# Retrieve the current book instance
    return render(request, 'relationship_app/library_detail.html', context)
    # context['average_rating'] = book.get_average_rating() 
# Create your views here.
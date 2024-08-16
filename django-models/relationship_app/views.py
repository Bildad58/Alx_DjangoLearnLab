from django.shortcuts import render
from .models import Book

from django.shortcuts import render
from .models import Book

def book_list(request):
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/book_list.html', context)
# def list_books(request):
#     book = Book.objects.all()
#     context = {
#         'book': book
#     }

#     return render(request, 'relationship_app/list_books.html', context)


def LibraryDetailView(self, request):

    context = {'detail_view': book}
    book = self.get_object()

    return render( request, 'relationship_app/library_detail.html', context)


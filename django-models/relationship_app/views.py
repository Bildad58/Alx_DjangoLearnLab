from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Library

def list_books(request):
    book = Library.object.all()
    context = {
        'book': book
    }

    return render(request, 'relationship_app/list_books.html', context)


def LibraryDetailView(self, request):

    context = {'detail_view': book}
    book = self.get_object()

    return render( request, 'relationship_app/library_detail.html', context)


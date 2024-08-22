from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import ExampleForm


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_create', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return HttpResponse
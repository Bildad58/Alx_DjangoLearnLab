from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


@permission_required('bookshelf.can_edit', raise_exception=True)
def my_view(request):
    return HttpResponse

@permission_required('bookshelf.can_delete', raise_exception=True)
def my_view(request):
    return HttpResponse

@permission_required('bookshelf.can_create', raise_exception=True)
def my_view(request):
    return HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def my_view(request):
    return HttpResponse
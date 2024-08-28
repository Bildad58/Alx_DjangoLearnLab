from django.urls import path
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Book', BookViewSet)


urlpatterns =[
    path('', BookViewSet, name = 'book_list')
    path('', include(router.urls)),
]
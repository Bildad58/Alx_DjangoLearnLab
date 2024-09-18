from django.urls import path, include
from .views import *


urlpatterns = [
    path('', notificationListView.as_view(), name='notifications'),
]
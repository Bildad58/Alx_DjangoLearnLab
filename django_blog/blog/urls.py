from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view() , name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/', PostUpdateView.as_view(), name='post-detail'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  

]







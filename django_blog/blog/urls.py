from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view() , name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    # path('tags/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),
    path(tags/<slug:tag_slug>/", "PostByTagListView.as_view()")
    path('search/', search_post, name='search'),
]
    
  









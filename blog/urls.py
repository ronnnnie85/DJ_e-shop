from django.urls import path, include

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='posts_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('blogs/new/', BlogCreateView.as_view(), name='post_create'),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
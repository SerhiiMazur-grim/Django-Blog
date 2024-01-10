from django.urls import path

from .views import PostsListView, PostDetailView


urlpatterns = [
    path('', PostsListView.as_view(), name='post_list'),
    path('post/<pk>/', PostDetailView.as_view(), name='post'),
]


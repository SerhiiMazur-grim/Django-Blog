from django.views.generic import ListView, DetailView

from .models import BlogPost


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog_posts/posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_posts/post.html'
    context_object_name = 'post'

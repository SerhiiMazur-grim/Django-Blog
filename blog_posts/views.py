from django.views.generic import ListView

from .models import BlogPost


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog_posts/posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

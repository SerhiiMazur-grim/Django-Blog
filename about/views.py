from django.views.generic import ListView

from .models import About


class AboutView(ListView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'abouts'
    ordering = ['-created_at']
    

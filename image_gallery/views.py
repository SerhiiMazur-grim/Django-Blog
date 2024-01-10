from django.views.generic import ListView

from .models import Image


class ImageGalleryView(ListView):
    model = Image
    template_name = 'image_gallery/image_gallery.html'
    context_object_name = 'images'
    ordering = ['-created_at']

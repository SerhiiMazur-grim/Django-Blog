from django.urls import path

from .views import ImageGalleryView


urlpatterns = [
    path('image_gallery/', ImageGalleryView.as_view(), name='image_gallery'),
]


from .models import Image


def images_context(request):
    images_context = Image.objects.all().order_by('-id')[:6]
    return {'images_context': images_context}

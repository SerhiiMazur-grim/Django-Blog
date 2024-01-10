from .models import Info, About


def info(request):
    info = Info.objects.get()
    return {'info': info}

def about_context(request):
    about_context = About.objects.get(title='About Me')
    return {'about_context': about_context}

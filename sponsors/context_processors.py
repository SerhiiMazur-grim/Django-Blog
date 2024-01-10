from .models import Sponsor


def sponsors_context(request):
    sponsors_list = Sponsor.objects.all()
    return {'sponsors_list': sponsors_list}

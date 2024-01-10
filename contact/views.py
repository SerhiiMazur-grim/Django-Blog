from django.views.generic import FormView

from .forms import ContactForm
from .models import Contact, ContactInfo


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/contact/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = ContactInfo.objects.last()
        context['contact_info'] = contact_info
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

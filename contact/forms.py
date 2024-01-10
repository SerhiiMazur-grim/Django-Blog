from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            'name': forms.TextInput(attrs={"id": "name", "name": "name", "class": "text"}),
            'email': forms.EmailInput(attrs={"id": "email", "name": "email", "class": "text"}),
            'message': forms.Textarea(attrs={"id": "message", "name": "message", "rows": "8", "cols": "50"}),
        }

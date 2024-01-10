from django.contrib import admin

from .models import Contact, ContactInfo


admin.site.register(Contact)
admin.site.register(ContactInfo)

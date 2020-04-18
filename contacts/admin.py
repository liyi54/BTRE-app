from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'listing', 'name', 'email', 'inquiry_date', 'phone']
    list_display_links = ['name', 'listing']
    search_fields = ['name', 'email', 'phone', 'listing']
    list_per_page = 25

admin.site.register(Contacts, ContactsAdmin)

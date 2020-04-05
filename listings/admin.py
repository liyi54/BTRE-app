from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'is_published', 'list_date', 'realtor']
    list_display_links = ['id', 'title']
    list_filter = ['realtor']
    list_editable = ['is_published']
    search_fields = ['id', 'title', 'city', 'state', 'zipcode']
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)


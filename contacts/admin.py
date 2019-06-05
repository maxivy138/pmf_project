from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone', 'message', 'contact_date')
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
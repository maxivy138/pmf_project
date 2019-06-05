from django.contrib import admin

from .models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'city', 'postalcode', 'phonenumber', 'borrowamount', 'contact_date')
    search_fields = ('name', 'email', 'city')
    list_per_page = 25

admin.site.register(Info, InfoAdmin)
from django.contrib import admin
from .models import ContactUs
# Register yofrur models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']
    
admin.site.register(ContactUs,ContactModelAdmin)
from django.contrib import admin

# Register your models here.

# pages/admin.py
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email', 'message')

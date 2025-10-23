from django.contrib import admin

# Register your models here.

# pages/admin.py
from django.contrib import admin
from .models import ContactMessage, FeedbackMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email', 'message')

@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'rating', 'date_sent')
    list_filter = ('rating', 'date_sent')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_sent',)

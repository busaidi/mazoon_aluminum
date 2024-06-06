from django.contrib import admin
from .models import Message


@admin.register(Message)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'message', 'created_at')
    search_fields = ('name', 'mobile', 'message')

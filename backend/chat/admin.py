from django.contrib import admin

from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'is_deleted')
    list_filter = ('is_deleted',)
    search_fields = ('text', 'user__username', 'user__phone')

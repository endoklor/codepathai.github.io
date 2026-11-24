from django.contrib import admin

from .models import AIInteractionLog


@admin.register(AIInteractionLog)
class AIInteractionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'mode', 'lesson', 'created_at')
    list_filter = ('mode',)
    search_fields = ('prompt', 'response', 'user__username')

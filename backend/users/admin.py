from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import Achievement, User, UserAchievement, UserProfile


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('phone', 'username', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('phone', 'username')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('phone', 'username', 'password')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'username', 'password1', 'password2'),
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'xp', 'streak', 'last_visit_date')
    search_fields = ('user__username', 'user__phone')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'description')


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'earned_at')

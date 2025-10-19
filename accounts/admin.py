from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'discord_id', 'steam_id', 'is_whitelisted', 'created_at']
    list_filter = ['is_whitelisted', 'created_at']
    search_fields = ['user__username', 'discord_id', 'steam_id']

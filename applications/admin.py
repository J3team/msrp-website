from django.contrib import admin
from .models import StaffApplication, WhitelistApplication

@admin.register(StaffApplication)
class StaffApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'status', 'created_at']
    list_filter = ['status', 'position', 'created_at']
    search_fields = ['user__username', 'experience', 'why_join']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'position', 'age', 'timezone', 'hours_available')
        }),
        ('Application Details', {
            'fields': ('experience', 'why_join', 'scenario_response', 'additional_info')
        }),
        ('Review', {
            'fields': ('status', 'reviewed_by', 'review_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(WhitelistApplication)
class WhitelistApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'character_name', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'character_name', 'character_backstory']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'character_name', 'character_age')
        }),
        ('Application Details', {
            'fields': ('character_backstory', 'rp_experience', 'scenario_response', 'referral', 'server_rules_read')
        }),
        ('Review', {
            'fields': ('status', 'reviewed_by', 'review_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

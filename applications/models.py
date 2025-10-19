from django.db import models
from django.contrib.auth.models import User

class StaffApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('under_review', 'Under Review'),
        ('interview', 'Interview Scheduled'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    POSITION_CHOICES = [
        ('moderator', 'Moderator'),
        ('admin', 'Administrator'),
        ('developer', 'Developer'),
        ('support', 'Support Staff'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_applications')
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    age = models.IntegerField()
    timezone = models.CharField(max_length=50)
    hours_available = models.CharField(max_length=200, help_text="How many hours per week can you dedicate?")
    experience = models.TextField(help_text="Previous moderation/staff experience")
    why_join = models.TextField(help_text="Why do you want to join our staff team?")
    scenario_response = models.TextField(help_text="How would you handle a player complaint?")
    additional_info = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_staff_applications')
    review_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_position_display()} Application"

class WhitelistApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whitelist_applications')
    character_name = models.CharField(max_length=100)
    character_age = models.IntegerField()
    character_backstory = models.TextField(help_text="Tell us about your character")
    rp_experience = models.TextField(help_text="Describe your roleplay experience")
    server_rules_read = models.BooleanField(default=False)
    scenario_response = models.TextField(help_text="How would you roleplay being pulled over?")
    referral = models.CharField(max_length=200, blank=True, help_text="How did you find our server?")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_whitelist_applications')
    review_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - Whitelist Application ({self.character_name})"

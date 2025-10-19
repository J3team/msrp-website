from django import forms
from .models import StaffApplication, WhitelistApplication

class StaffApplicationForm(forms.ModelForm):
    class Meta:
        model = StaffApplication
        fields = ['position', 'age', 'timezone', 'hours_available', 'experience', 'why_join', 'scenario_response', 'additional_info']
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 4}),
            'why_join': forms.Textarea(attrs={'rows': 4}),
            'scenario_response': forms.Textarea(attrs={'rows': 4}),
            'additional_info': forms.Textarea(attrs={'rows': 3}),
        }

class WhitelistApplicationForm(forms.ModelForm):
    class Meta:
        model = WhitelistApplication
        fields = ['character_name', 'character_age', 'character_backstory', 'rp_experience', 'scenario_response', 'referral', 'server_rules_read']
        widgets = {
            'character_backstory': forms.Textarea(attrs={'rows': 5}),
            'rp_experience': forms.Textarea(attrs={'rows': 4}),
            'scenario_response': forms.Textarea(attrs={'rows': 4}),
        }

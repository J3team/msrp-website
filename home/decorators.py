from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def staff_required(view_func):
    """Decorator to require staff permissions"""
    def check_staff(user):
        return user.is_authenticated and user.is_staff

    decorated_view = user_passes_test(check_staff, login_url='login')(view_func)
    return decorated_view

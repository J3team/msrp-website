from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StaffApplication, WhitelistApplication
from .forms import StaffApplicationForm, WhitelistApplicationForm

@login_required
def apply_staff(request):
    existing_app = StaffApplication.objects.filter(user=request.user, status='pending').first()
    if existing_app:
        messages.warning(request, 'You already have a pending staff application.')
        return redirect('home')

    if request.method == 'POST':
        form = StaffApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, 'Your staff application has been submitted! We will review it soon.')
            return redirect('home')
    else:
        form = StaffApplicationForm()

    return render(request, 'applications/staff_apply.html', {'form': form})

@login_required
def apply_whitelist(request):
    existing_app = WhitelistApplication.objects.filter(user=request.user, status='pending').first()
    if existing_app:
        messages.warning(request, 'You already have a pending whitelist application.')
        return redirect('home')

    if request.method == 'POST':
        form = WhitelistApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, 'Your whitelist application has been submitted! We will review it soon.')
            return redirect('home')
    else:
        form = WhitelistApplicationForm()

    return render(request, 'applications/whitelist_apply.html', {'form': form})

@login_required
def my_applications(request):
    staff_apps = StaffApplication.objects.filter(user=request.user)
    whitelist_apps = WhitelistApplication.objects.filter(user=request.user)

    context = {
        'staff_apps': staff_apps,
        'whitelist_apps': whitelist_apps,
    }
    return render(request, 'applications/my_applications.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Q
from shop.models import ShopItem, Purchase
from tickets.models import Ticket
from applications.models import StaffApplication, WhitelistApplication
from django.contrib.auth.models import User
from .decorators import staff_required

def home(request):
    featured_items = ShopItem.objects.filter(is_active=True)[:6]
    context = {
        'featured_items': featured_items,
    }
    return render(request, 'home/index.html', context)

@staff_required
def admin_dashboard(request):
    """Main admin dashboard"""
    context = {
        'total_users': User.objects.count(),
        'total_tickets': Ticket.objects.count(),
        'open_tickets': Ticket.objects.filter(status='open').count(),
        'pending_staff_apps': StaffApplication.objects.filter(status='pending').count(),
        'pending_whitelist_apps': WhitelistApplication.objects.filter(status='pending').count(),
        'total_purchases': Purchase.objects.count(),
        'recent_tickets': Ticket.objects.all()[:5],
        'recent_purchases': Purchase.objects.all()[:5],
    }
    return render(request, 'admin_panel/dashboard.html', context)

@staff_required
def admin_tickets(request):
    """Manage all tickets"""
    status_filter = request.GET.get('status', 'all')

    tickets = Ticket.objects.all()
    if status_filter != 'all':
        tickets = tickets.filter(status=status_filter)

    context = {
        'tickets': tickets,
        'status_filter': status_filter,
    }
    return render(request, 'admin_panel/tickets.html', context)

@staff_required
def admin_ticket_manage(request, pk):
    """Manage specific ticket"""
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'assign':
            ticket.assigned_to = request.user
            ticket.status = 'in_progress'
            ticket.save()
            messages.success(request, 'Ticket assigned to you!')

        elif action == 'status':
            new_status = request.POST.get('status')
            ticket.status = new_status
            ticket.save()
            messages.success(request, f'Ticket status updated to {ticket.get_status_display()}')

        elif action == 'priority':
            new_priority = request.POST.get('priority')
            ticket.priority = new_priority
            ticket.save()
            messages.success(request, f'Ticket priority updated to {ticket.get_priority_display()}')

        return redirect('admin_ticket_manage', pk=pk)

    context = {'ticket': ticket}
    return render(request, 'admin_panel/ticket_manage.html', context)

@staff_required
def admin_applications(request):
    """Manage applications"""
    app_type = request.GET.get('type', 'staff')

    if app_type == 'staff':
        applications = StaffApplication.objects.all()
    else:
        applications = WhitelistApplication.objects.all()

    context = {
        'applications': applications,
        'app_type': app_type,
    }
    return render(request, 'admin_panel/applications.html', context)

@staff_required
def admin_application_review(request, app_type, pk):
    """Review specific application"""
    if app_type == 'staff':
        application = get_object_or_404(StaffApplication, pk=pk)
    else:
        application = get_object_or_404(WhitelistApplication, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')
        notes = request.POST.get('review_notes', '')

        if action == 'approve':
            if app_type == 'staff':
                application.status = 'accepted'
            else:
                application.status = 'approved'
                # Also set user as whitelisted
                application.user.profile.is_whitelisted = True
                application.user.profile.save()
            application.reviewed_by = request.user
            application.review_notes = notes
            application.save()
            messages.success(request, 'Application approved!')

        elif action == 'reject':
            application.status = 'rejected'
            application.reviewed_by = request.user
            application.review_notes = notes
            application.save()
            messages.warning(request, 'Application rejected.')

        elif action == 'interview':
            application.status = 'interview'
            application.reviewed_by = request.user
            application.review_notes = notes
            application.save()
            messages.info(request, 'Application moved to interview stage.')

        return redirect('admin_applications')

    context = {
        'application': application,
        'app_type': app_type,
    }
    return render(request, 'admin_panel/application_review.html', context)

@staff_required
def admin_users(request):
    """Manage users"""
    search = request.GET.get('search', '')

    users = User.objects.all()
    if search:
        users = users.filter(
            Q(username__icontains=search) |
            Q(email__icontains=search) |
            Q(profile__discord_id__icontains=search)
        )

    context = {
        'users': users,
        'search': search,
    }
    return render(request, 'admin_panel/users.html', context)

@staff_required
def admin_user_manage(request, pk):
    """Manage specific user"""
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'whitelist':
            user.profile.is_whitelisted = not user.profile.is_whitelisted
            user.profile.save()
            status = "whitelisted" if user.profile.is_whitelisted else "removed from whitelist"
            messages.success(request, f'User {status}!')

        elif action == 'staff':
            user.is_staff = not user.is_staff
            user.save()
            status = "granted staff" if user.is_staff else "removed staff"
            messages.success(request, f'User {status} permissions!')

        return redirect('admin_user_manage', pk=pk)

    context = {'user_profile': user}
    return render(request, 'admin_panel/user_manage.html', context)

@staff_required
def admin_shop(request):
    """Manage shop items and purchases"""
    view_type = request.GET.get('view', 'items')

    if view_type == 'items':
        items = ShopItem.objects.all()
        context = {'items': items, 'view_type': view_type}
    else:
        purchases = Purchase.objects.all()
        context = {'purchases': purchases, 'view_type': view_type}

    return render(request, 'admin_panel/shop.html', context)

@staff_required
def admin_purchase_manage(request, pk):
    """Manage specific purchase"""
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        purchase.status = new_status
        purchase.save()
        messages.success(request, f'Purchase status updated to {purchase.get_status_display()}!')
        return redirect('admin_shop') + '?view=purchases'

    context = {'purchase': purchase}
    return render(request, 'admin_panel/purchase_manage.html', context)

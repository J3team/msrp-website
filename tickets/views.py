from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, TicketMessage
from .forms import TicketCreateForm, TicketMessageForm

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    context = {'tickets': tickets}
    return render(request, 'tickets/ticket_list.html', context)

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Your ticket has been created! Our staff will respond soon.')
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketCreateForm()
    return render(request, 'tickets/ticket_create.html', {'form': form})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TicketMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.ticket = ticket
            message.user = request.user
            message.save()
            messages.success(request, 'Your message has been added.')
            return redirect('ticket_detail', pk=pk)
    else:
        form = TicketMessageForm()

    context = {
        'ticket': ticket,
        'form': form
    }
    return render(request, 'tickets/ticket_detail.html', context)

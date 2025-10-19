from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ShopItem, Purchase, Category

def shop_index(request):
    categories = Category.objects.all()
    items = ShopItem.objects.filter(is_active=True)

    category_filter = request.GET.get('category')
    if category_filter:
        items = items.filter(category__id=category_filter)

    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'shop/shop_index.html', context)

def shop_item_detail(request, pk):
    item = get_object_or_404(ShopItem, pk=pk, is_active=True)
    context = {'item': item}
    return render(request, 'shop/shop_item_detail.html', context)

@login_required
def purchase_item(request, pk):
    item = get_object_or_404(ShopItem, pk=pk, is_active=True)

    if not item.in_stock:
        messages.error(request, 'This item is out of stock.')
        return redirect('shop_item_detail', pk=pk)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if item.stock != -1 and quantity > item.stock:
            messages.error(request, 'Not enough stock available.')
            return redirect('shop_item_detail', pk=pk)

        total_price = item.price * quantity

        purchase = Purchase.objects.create(
            user=request.user,
            item=item,
            quantity=quantity,
            total_price=total_price,
            status='pending'
        )

        if item.stock != -1:
            item.stock -= quantity
            item.save()

        messages.success(request, f'Purchase successful! Your order #{purchase.id} is being processed.')
        return redirect('purchase_history')

    return redirect('shop_item_detail', pk=pk)

@login_required
def purchase_history(request):
    purchases = Purchase.objects.filter(user=request.user)
    context = {'purchases': purchases}
    return render(request, 'shop/purchase_history.html', context)

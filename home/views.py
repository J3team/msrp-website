from django.shortcuts import render
from shop.models import ShopItem

def home(request):
    featured_items = ShopItem.objects.filter(is_active=True)[:6]
    context = {
        'featured_items': featured_items,
    }
    return render(request, 'home/index.html', context)

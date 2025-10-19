from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_index, name='shop_index'),
    path('item/<int:pk>/', views.shop_item_detail, name='shop_item_detail'),
    path('purchase/<int:pk>/', views.purchase_item, name='purchase_item'),
    path('history/', views.purchase_history, name='purchase_history'),
]

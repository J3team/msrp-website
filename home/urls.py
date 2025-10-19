from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Admin Panel URLs
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/tickets/', views.admin_tickets, name='admin_tickets'),
    path('admin-panel/tickets/<int:pk>/', views.admin_ticket_manage, name='admin_ticket_manage'),
    path('admin-panel/applications/', views.admin_applications, name='admin_applications'),
    path('admin-panel/applications/<str:app_type>/<int:pk>/', views.admin_application_review, name='admin_application_review'),
    path('admin-panel/users/', views.admin_users, name='admin_users'),
    path('admin-panel/users/<int:pk>/', views.admin_user_manage, name='admin_user_manage'),
    path('admin-panel/shop/', views.admin_shop, name='admin_shop'),
    path('admin-panel/shop/purchase/<int:pk>/', views.admin_purchase_manage, name='admin_purchase_manage'),
]

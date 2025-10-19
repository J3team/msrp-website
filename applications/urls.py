from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.apply_staff, name='apply_staff'),
    path('whitelist/', views.apply_whitelist, name='apply_whitelist'),
    path('my-applications/', views.my_applications, name='my_applications'),
]

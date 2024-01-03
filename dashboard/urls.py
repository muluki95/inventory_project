from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard_index'),
    path('staff/', views.staff, name = 'dashboard_staff'),
    path('products/', views.products, name = 'dashboard_products'),
    path('orders/', views.orders, name = 'dashboard_orders')

]
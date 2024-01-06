from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard_index'),
    path('staff/', views.staff, name = 'dashboard_staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name = 'dashboard_staff_detail'),
    path('products/', views.products, name = 'dashboard_products'),
    path('products/delete/<int:pk>/', views.product_delete, name = 'dashboard_products_delete'),
    path('products/update/<int:pk>/', views.product_update, name = 'dashboard_products_update'),
    path('orders/', views.order, name = 'dashboard_orders')

]
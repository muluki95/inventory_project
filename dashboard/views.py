from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import Product, Order
from dashboard.forms import ProductForm, OrderForm
from django.contrib.auth.models import User
 

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    if request.method == "POST":
         form = OrderForm(request.POST)
         if form.is_valid():
              instance = form.save(commit=False)
              instance.staff = request.user                   #assigns the staff to the order being made
              instance.save()
              return redirect('dashboard_index')
    else:
         form = OrderForm()
    context={
         'orders':orders,
         'form':form,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    employees = User.objects.all()
    context={
         "employees" : employees
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request, pk):
     employee = User.objects.get(id=pk)
     context = {
          "employee" : employee
     }
     return render(request, 'dashboard/staff_detail.html', context)
@login_required(login_url='user-login')
def products(request):
    items = Product.objects.all() #Using object relational mapping
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            return redirect('dashboard_products')
        
    else:
        form = ProductForm()    
    context = {
        'items' : items,
        'form': form,
    }
    return render(request, 'dashboard/products.html', context)

def product_delete(request, pk):
        item = Product.objects.get(id=pk)
        if request.method == 'POST':
             item.delete()
             return redirect('dashboard_products')
        context = {
        'item': item
        }
        return render(request, 'dashboard/products_delete.html', context)

def product_update(request, pk):
     item = Product.objects.get(id=pk)
     if request.method == 'POST':
          form = ProductForm(request.POST, instance=item)
          if form.is_valid():
               form.save()
               return redirect('dashboard_products')
     else:
          form = ProductForm(instance=item)
          context={
               "form": form
          }
               
          
     return render(request, 'dashboard/products_update.html', context)

        
        


@login_required(login_url='user-login')
def order(request):
    user_orders = Order.objects.all()
    context = {
         'user_orders': user_orders
         }
    return render(request, 'dashboard/orders.html', context)

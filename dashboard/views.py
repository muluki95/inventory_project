from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import Product, Order
from dashboard.forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
 

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    items_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    employees_count = User.objects.all().count()

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
         'products':products,
         'items_count':items_count,
         'orders_count':orders_count,
         'employees_count':employees_count
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    employees = User.objects.all()
    items_count = Product.objects.all().count()
    employees_count = employees.count()     #dynamically rendering the staff number on the dashboard
    orders_count = Order.objects.all().count()

    context= {
         "employees" : employees,
         "employees_count": employees_count,
         "orders_count": orders_count,
         "items_count": items_count
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request, pk):
     employee = User.objects.get(id=pk)
     context = {
          "employee" : employee,

     }
     return render(request, 'dashboard/staff_detail.html', context)
@login_required(login_url='user-login')
def products(request):
    items = Product.objects.all() #Using object relational mapping
    items_count = items.count()
    orders_count = Order.objects.all().count()
    employees_count = User.objects.all().count()  #shows the numbers of staff and orders even when you click on products box
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            product_name = form.cleaned_data.get('name')  #dictionary coontaining the cleaned form data
            messages.success(request,f'{product_name} has been added')   
            return redirect('dashboard_products')
        
    else:
        form = ProductForm()    
    context = {
        'items' : items,
        'form': form,
        'employees_count': employees_count,
        'orders_count': orders_count,
        'items_count': items_count
       


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
    orders_count = user_orders.count()
    employees_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
         'user_orders': user_orders,
         'employees_count' : employees_count,
         'orders_count' : orders_count,
         'items_count' : items_count

         }
    return render(request, 'dashboard/orders.html', context)

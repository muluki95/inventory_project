from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import Product
#from .forms import ProductForm
 

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def products(request):
 #   items = Product.objects.all()
 #   if request.method == 'POST':
 #       form = ProductForm(request.POST)
 #      if form.is_valid():
 #           new_item = form.save(commit=False)
 #           new_item.author = request.user
 #           new_item.save()
 #           return index(request)
        
 #   else:
 #       form = ProductForm()    
 #   context = {
 #       'items' : items,
 #   }
    return render(request, 'dashboard/products.html')

@login_required(login_url='user-login')
def orders(request):
    return render(request, 'dashboard/orders.html')

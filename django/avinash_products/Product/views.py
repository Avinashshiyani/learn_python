from django.shortcuts import render , redirect , get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request , 'product_form.html' , {'form':form})

def product_list(request):
    products = Product.objects.all()
    return render(request , 'product_list.html' , {'products':products})

def product_update(request , id):
    product = get_object_or_404(Product , id = id)
    form = ProductForm(request.POST or None , instance = product)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request , 'product_form.html' , {'form':form})

def product_delete(request , id):
    product =  get_object_or_404(Product , id = id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request , 'product_confirm_delete.html' , {'product':product})

    
    
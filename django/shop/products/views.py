from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('product_list')
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'
    success_url = reverse_lazy('product_list')
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('product_list')


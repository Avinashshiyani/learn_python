from django.urls import path
from .views import ProductListView , ProductCreateView , ProductUpdateView , ProductDeleteView

urlpatterns = [
    path('',ProductListView.as_view() , name='product_list'),
    path('add/',ProductCreateView.as_view() , name='add_product'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]

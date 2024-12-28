from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_mobile, name='add_mobile'),
    path('display/', views.display_mobiles, name='display_mobiles'),
    path('<int:pk>/delete/', views.delete_mobile, name='delete_mobile'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view , name = "login"),
    path('records/', views.patient_records , name = "records"),
    path('delete/<id>', views.delete_data , name = "delete_data"),
    path('logout/', views.login_view , name = "logout"),
]
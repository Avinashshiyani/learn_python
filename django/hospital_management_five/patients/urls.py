from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view , name = 'login'),
    path('patient_records/', views.patient_records , name = 'patient_records'),
    path('logout/', views.logout_view , name = 'logout'),
]
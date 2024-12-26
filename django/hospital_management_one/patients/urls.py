from django.urls import path
from .import views

urlpatterns = [
    path('login/' , views.login_view , name = 'login'),
    path('records/' , views.patient_records , name = 'patient_records'),
    path('logout/' , views.logout_view , name = 'logout')
]
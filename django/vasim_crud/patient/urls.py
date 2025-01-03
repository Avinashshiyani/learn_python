from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view , name = 'login'),
    path('records/', views.patient_record , name = 'records'),
    path('logout/', views.logout_view , name = 'logout'),
    path('delete/<id>', views.delete , name = 'delete'),
]
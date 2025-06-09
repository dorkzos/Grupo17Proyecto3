# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mi-cuenta/', views.mi_cuenta_view, name='mi_cuenta'),
    path('mis-pedidos/', views.mis_pedidos_view, name='mis_pedidos'),
]
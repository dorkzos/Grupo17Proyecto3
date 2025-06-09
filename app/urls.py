
# app/urls.py sofi 
# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
]
=======
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mi-cuenta/', views.mi_cuenta_view, name='mi_cuenta'),
    path('mis-pedidos/', views.mis_pedidos_view, name='mis_pedidos'),
]
>>>>>>> 14e79acad0ce44676ea22f5bf0b03807b102201d

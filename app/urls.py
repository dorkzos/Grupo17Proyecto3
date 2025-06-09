# app/urls.py sofi 
# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo_libros, name='catalogo_libros'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar-al-carrito/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mi-cuenta/', views.mi_cuenta_view, name='mi_cuenta'),
    path('mis-pedidos/', views.mis_pedidos_view, name='mis_pedidos'),
]



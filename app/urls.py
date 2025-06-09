# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('logout/', views.usuario_logout, name='usuario_logout'),
    path('catalogo/', views.catalogo_libros, name='catalogo_libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_al_carrito/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('pagar/', views.pagar, name='pagar'),
    path('historial/', views.historial_compras, name='historial_compras'),
    path('libro/<int:libro_id>/agregar_resena/', views.agregar_resena, name='agregar_resena'),
    path('libro/<int:libro_id>/ver_resenas/', views.ver_resenas, name='ver_resenas'),
]



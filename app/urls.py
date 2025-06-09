
# app/urls.py sofi 
from django.urls import path
from . import views

urlpatterns = [
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
]

from django.urls import path
from .views import inicio, usuario_logout

urlpatterns = [
    path('', inicio, name='inicio'),              
    path('inicio/', inicio, name='inicio_url'),   
    path('logout/', usuario_logout, name='usuario_logout'),
]

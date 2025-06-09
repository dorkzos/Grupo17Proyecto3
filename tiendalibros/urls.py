from django.urls import path
from .views import inicio, usuario_logout, registrarse

urlpatterns = [
    path('', inicio, name='inicio'),              
    path('inicio/', inicio, name='inicio_url'),   
    path('logout/', usuario_logout, name='usuario_logout'),
    path('registrarse/', registrarse, name='registrarse'),
]

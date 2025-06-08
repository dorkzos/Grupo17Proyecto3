from django.contrib import admin
from .models import Autor, Libro, Pedido, DetallePedido, Historial

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Historial)
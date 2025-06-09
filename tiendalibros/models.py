from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo}"


class Historial(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(default=0, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)
    accion = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username if self.usuario else ''} - {self.titulo} x {self.cantidad} - {self.accion}"


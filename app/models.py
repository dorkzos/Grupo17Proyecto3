from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(default=0)
    fecha_publicacion = models.DateField(null=True, blank=True)

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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
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

class CarritoUser(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('usuario', 'libro')

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo} x {self.cantidad}"

class CarritoActual(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(default=0)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} - {self.titulo} x {self.cantidad}"

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    comentario = models.TextField()
    calificacion = models.IntegerField(choices=[(1, '1 - Muy mala'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - Muy buena')], default=5)

    def __str__(self):
        return f"Reseña de {self.libro.titulo}: {self.comentario[:30]}... ({self.calificacion})"
from django.db import models
from django.contrib.auth.models import User

#
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(default=0)
    # otros campos necesarios

    def __str__(self):
        return self.titulo

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
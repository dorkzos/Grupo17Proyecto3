from django.db import models

#
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    # otros campos necesarios

    def __str__(self):
        return self.titulo
from django.db import models

# Create your models here.

class Libros  (models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    seudonimo = models.CharField(max_length=35,  default='Escritor')

    def __str__(self) -> str:
        return self.nombre + ' ' + '('+ str(self.codigo) +')'

    class Meta:
        verbose_name_plural = "libros" 
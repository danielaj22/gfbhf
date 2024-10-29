from django.db import models

# Create your models here.
class sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    ciudad=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    id_venta=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="sucursal"
        verbose_name_plural="sucursales"
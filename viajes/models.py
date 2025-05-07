from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)


class Iterinario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    destinos = models.ManyToManyField(Destino)
    fecha_inicio = models.DateField()
    fecha_salida = models.DateField()
    compartir_con = models.ManyToManyField(User, related_name='itinerarios_compartidos', blank=True)


    
class Reserva(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('A', 'Cancelada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Iterinario = models.ForeignKey(Iterinario, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    detalles = models.TextField(blank=True)
    
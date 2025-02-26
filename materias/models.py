from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.nombre
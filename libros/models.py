from django.db import models
from django.contrib.auth.models import User
from materias.models import Materia

# Create your models here.
class Libro(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    publisher = models.CharField(max_length=100, verbose_name='Editorial')
    materia = models.ForeignKey(Materia, verbose_name='Materia', default=1, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='Cantidad')
    author = models.CharField(max_length=100, verbose_name='Autor')
    isbn = models.IntegerField(verbose_name='ISBN')  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.title
    
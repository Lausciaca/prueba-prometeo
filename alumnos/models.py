from django.db import models

# Create your models here.
class Curso(models.Model):
    name = models.IntegerField(verbose_name='Curso')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return str(self.name)
    
class Division(models.Model):
    name = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):  
        return f" {self.curso} {self.name}"

class CDE(models.Model):
    content= models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.created
    
class Inscripcion(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100)
    content = models.TextField(verbose_name='Contenido')
    link = models.URLField(verbose_name='Link a formulario', max_length=200)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.title
    
class Examen(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100)
    inscription_start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de inicio de inscripcion')
    inscription_end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de fin de inscripcion')
    test_start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de inicio de examenes')
    test_end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de fin de examenes')
    content = models.TextField(verbose_name='Contenido')
    link = models.URLField(verbose_name='Link formulario', max_length=250)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.title
    
class Horario(models.Model):
    division = models.ForeignKey(Division, verbose_name='Curso/Division', on_delete=models.CASCADE)
    link = models.URLField(verbose_name='Link a horario', max_length=200)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return f"Horario de {self.division}"
    
    
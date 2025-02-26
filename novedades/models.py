from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Novedad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    slug = models.SlugField(verbose_name='Slug', unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(verbose_name='Orden', default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Solo generar slug si está vacío
            self.slug = slugify(self.title)
            # Verificar si existe un slug duplicado y ajustarlo
            original_slug = self.slug
            queryset = Novedad.objects.filter(slug=self.slug)
            counter = 1
            while queryset.exists():
                self.slug = f"{original_slug}-{counter}"
                queryset = Novedad.objects.filter(slug=self.slug)
                counter += 1

        super(Novedad, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

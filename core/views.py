from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from novedades.models import Novedad

class HomePageView(ListView):
    model = Novedad
    template_name = 'core/home.html'
    context_object_name = 'novedades'  # Opcional: para usar un nombre más descriptivo en el template

    def get_queryset(self):
        # Ordena las novedades por fecha en orden descendente y toma las últimas 4
        return Novedad.objects.all().order_by('-created')[:3]
    
class InstitucionPageView(TemplateView):
    template_name = 'core/institucion.html'
    
class SecretariaPageView(TemplateView):
    template_name = 'core/secretaria.html'
    
class ContactoPageView(TemplateView):
    template_name = 'core/contacto.html'
    
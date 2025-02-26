from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from novedades.models import Novedad

# Create your views here.
class HomePageView(ListView):
    model = Novedad
    template_name = 'core/home.html'
    
class InstitucionPageView(TemplateView):
    template_name = 'core/institucion.html'
    
class SecretariaPageView(TemplateView):
    template_name = 'core/secretaria.html'
    
class ContactoPageView(TemplateView):
    template_name = 'core/contacto.html'
    
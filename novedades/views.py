from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Novedad
from .forms import NovedadForm

# Create your views here.
class NovedadDetailView(DetailView):
    model = Novedad
    template_name = 'novedades/novedad.html'
    
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Novedad, slug=slug)  # Recupera el objeto utilizando el slug
    
class NovedadCreateView(CreateView):
    model = Novedad
    template_name = 'novedades/novedad_create.html'
    form_class = NovedadForm
    success_url = reverse_lazy('home')
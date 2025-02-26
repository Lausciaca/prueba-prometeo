from django.shortcuts import render, get_object_or_404
from modalidades.models import Modalidad
from django.views.generic.detail import DetailView


# Create your views here.
class ModalidadPageView(DetailView):
    model = Modalidad
    template_name = 'modalidades/modalidad_detail.html'
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Modalidad, slug=slug)  # Recupera el objeto utilizando el slug
    
    
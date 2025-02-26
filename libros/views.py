from django.shortcuts import render
from .models import Libro
from materias.models import Materia
from django.views.generic.list import ListView

# Create your views here.
class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/biblioteca.html'
    context_object_name = 'libros'

    def get_queryset(self):
        # Obtener los libros
        queryset = super().get_queryset()

        # Filtrar por búsqueda
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(title__icontains=query)

        # Filtrar por autor
        selected_authors = self.request.GET.getlist('author')
        if selected_authors:
            queryset = queryset.filter(author__in=selected_authors)

        # Filtrar por materia
        selected_materias = self.request.GET.getlist('materia')
        if selected_materias:
            queryset = queryset.filter(materia__nombre__in=selected_materias)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener lista de autores únicos y materias
        context['autores'] = (
                    Libro.objects
                    .values_list('author', flat=True)
                    .distinct()
                    .order_by('author')[:5]
                )        
        context['materias'] = Materia.objects.all()

        # Conservar los valores de búsqueda y filtros
        context['query'] = self.request.GET.get('q', '')
        context['selected_authors'] = self.request.GET.getlist('author')
        context['selected_materias'] = self.request.GET.getlist('materia')

        return context

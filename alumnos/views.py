from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CDE, Inscripcion, Examen, Horario


# Create your views here.
class CDEPageView(ListView):
    model = CDE
    template_name = 'alumnos/centro_de_estudiantes.html'
    
class InscripcionesPageView(ListView):
    model = Inscripcion
    template_name = 'alumnos/inscripciones.html'
    
class ExamenesPageView(ListView):
    model = Examen
    template_name = 'alumnos/examenes.html'
    
class HorariosPageView(ListView):
    model = Horario
    template_name = 'alumnos/horarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        horarios = Horario.objects.all()

        # Imprimir todos los horarios para verificar su formato
        print("Todos los horarios:")
        for horario in horarios:
            print(str(horario))

        # Filtramos los horarios basados en el nombre de la división
        context["primero"] = [horario for horario in horarios if "1" in str(horario)]
        context["segundo"] = [horario for horario in horarios if "2" in str(horario)]
        context["tercero"] = [horario for horario in horarios if "3" in str(horario)]
        context["cuarto"] = [horario for horario in horarios if "4" in str(horario)]
        context["quinto"] = [horario for horario in horarios if "5" in str(horario)]
        context["sexto"] = [horario for horario in horarios if "6" in str(horario)]

        # Imprimir la cantidad de horarios en cada lista para verificar
        print(f"Primero: {len(context['primero'])}, Segundo: {len(context['segundo'])}, Tercero: {len(context['tercero'])}, Cuarto: {len(context['cuarto'])}, Quinto: {len(context['quinto'])}, Sexto: {len(context['sexto'])}")

        return context

from django.urls import path, include
from .views import CDEPageView, InscripcionesPageView, ExamenesPageView, HorariosPageView

urlpatterns = [
    path('centro-de-estudiantes', CDEPageView.as_view(), name="alumnos_centro-de-estudiantes"),
    path('inscripciones', InscripcionesPageView.as_view(), name="alumnos_inscripciones"),
    path('examenes', ExamenesPageView.as_view(), name="alumnos_examenes"),
    path('horarios', HorariosPageView.as_view(), name="alumnos_horarios"),
    path('modalidades/', include('modalidades.urls')),
]
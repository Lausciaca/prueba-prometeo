from django.urls import path
from .views import ModalidadPageView

urlpatterns = [
    path('<slug:slug>/', ModalidadPageView.as_view(), name="alumnos_modalidades"),
]
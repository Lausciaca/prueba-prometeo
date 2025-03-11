from django.urls import path
from .views import NovedadDetailView, NovedadCreateView

urlpatterns = [
    path('create/', NovedadCreateView.as_view(), name="novedad_create"),
    path('<slug:slug>/', NovedadDetailView.as_view(), name="novedad"),
]

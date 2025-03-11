from django.urls import path, include
from .views import HomePageView, InstitucionPageView, SecretariaPageView, ContactoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('institucion', InstitucionPageView.as_view(), name="institucion"),
    path('alumnos/', include('alumnos.urls')),
    path('biblioteca', include('libros.urls')),
    path('secretaria', SecretariaPageView.as_view(), name='secretaria'),
    path('contacto', ContactoPageView.as_view(), name='contacto'),
]

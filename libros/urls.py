from django.urls import path
from .views import LibrosListView

urlpatterns = [
    path('', LibrosListView.as_view(), name="biblioteca"),
]
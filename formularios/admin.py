from django.contrib import admin
from .models import Formulario

# Register your models here.
class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

admin.site.register(Formulario, FormularioAdmin)
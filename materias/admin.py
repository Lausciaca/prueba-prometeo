from django.contrib import admin
from .models import Materia

# Register your models here.
class MateriaAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
admin.site.register(Materia, MateriaAdmin)
from django.contrib import admin
from .models import Modalidad

# Register your models here.
class ModalidadAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
admin.site.register(Modalidad, ModalidadAdmin)
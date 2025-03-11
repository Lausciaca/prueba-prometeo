from django.contrib import admin
from .models import Novedad

# Register your models here.
class NovedadAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated', 'slug', 'order']
    
admin.site.register(Novedad, NovedadAdmin)
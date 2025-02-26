from django.contrib import admin
from .models import CDE, Horario, Curso, Division, Inscripcion, Examen

# Register your models here.
class CDEAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(CDE, CDEAdmin)


class HorarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Horario, HorarioAdmin)


class InscripcionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Inscripcion, InscripcionAdmin)


class ExamenAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Examen, ExamenAdmin)


class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Curso, CursoAdmin)


class DivisionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Division, DivisionAdmin)

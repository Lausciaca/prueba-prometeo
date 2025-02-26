from django import forms
from .models import Novedad
from ckeditor.widgets import CKEditorWidget  # Importar el widget de CKEditor


class NovedadForm(forms.ModelForm):
    
    
    class Meta:
        model = Novedad
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'title-form'}, ),
            'content': CKEditorWidget(attrs={'class':'content-form'})
        }
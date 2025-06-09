
from django import forms
from .models import Libro  # Asegúrate de tener este modelo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

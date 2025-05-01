from django import forms
from .models import Desayuno

class DesayunoForm(forms.ModelForm):
    class Meta:
        model = Desayuno
        fields = ['nombre', 'descripcion', 'precio', 'disponible']

from django import forms
from .models import Plant

#Creating form class
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields ="__all__"
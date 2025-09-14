from django import forms
from .models import Equipement
from apps.coachs.models import Coach
from core.enums import EquipmentStatus, EquipmentType

class EquipementForm(forms.ModelForm):
    coach = forms.ModelChoiceField(
        queryset=Coach.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Coach assigné"
    )

    class Meta:
        model = Equipement
        fields = ['nom', 'type', 'statut', 'coach']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}, choices=EquipmentType.choices),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nom': 'Nom de l\'équipement',
            'type': 'Type d\'équipement',
            'statut': 'Statut',
            'coach': 'Coach assigné'
        }

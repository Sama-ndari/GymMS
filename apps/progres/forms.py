from django import forms
from .models import Progres
from apps.users.models import User
from core.enums import UserRole
import json

class ProgresForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=User.objects.filter(role=UserRole.CLIENT),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Client"
    )
    
    # Individual measurement fields
    tour_taille = forms.DecimalField(
        max_digits=5, decimal_places=1, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label="Tour de taille (cm)"
    )
    tour_poitrine = forms.DecimalField(
        max_digits=5, decimal_places=1, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label="Tour de poitrine (cm)"
    )
    tour_bras = forms.DecimalField(
        max_digits=5, decimal_places=1, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label="Tour de bras (cm)"
    )
    tour_cuisse = forms.DecimalField(
        max_digits=5, decimal_places=1, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label="Tour de cuisse (cm)"
    )
    masse_grasse = forms.DecimalField(
        max_digits=5, decimal_places=1, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label="Masse grasse (%)"
    )
    
    class Meta:
        model = Progres
        fields = ['client', 'date', 'notes', 'poids']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'poids': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }
        labels = {
            'date': 'Date du suivi',
            'notes': 'Notes sur les progrès',
            'poids': 'Poids (kg)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If editing existing progress, populate measurement fields
        if self.instance and self.instance.pk and self.instance.mesures:
            try:
                mesures = self.instance.mesures
                if isinstance(mesures, str):
                    mesures = json.loads(mesures)
                
                self.fields['tour_taille'].initial = mesures.get('tour_taille')
                self.fields['tour_poitrine'].initial = mesures.get('tour_poitrine')
                self.fields['tour_bras'].initial = mesures.get('tour_bras')
                self.fields['tour_cuisse'].initial = mesures.get('tour_cuisse')
                self.fields['masse_grasse'].initial = mesures.get('masse_grasse')
            except (json.JSONDecodeError, TypeError):
                pass
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Build measurements JSON from individual fields
        mesures = {}
        if self.cleaned_data.get('tour_taille'):
            mesures['tour_taille'] = float(self.cleaned_data['tour_taille'])
        if self.cleaned_data.get('tour_poitrine'):
            mesures['tour_poitrine'] = float(self.cleaned_data['tour_poitrine'])
        if self.cleaned_data.get('tour_bras'):
            mesures['tour_bras'] = float(self.cleaned_data['tour_bras'])
        if self.cleaned_data.get('tour_cuisse'):
            mesures['tour_cuisse'] = float(self.cleaned_data['tour_cuisse'])
        if self.cleaned_data.get('masse_grasse'):
            mesures['masse_grasse'] = float(self.cleaned_data['masse_grasse'])
        
        instance.mesures = mesures if mesures else None
        
        if commit:
            instance.save()
        return instance

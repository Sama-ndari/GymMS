from django import forms
from .models import Reservation
from apps.users.models import User
from apps.coachs.models import Coach
from core.enums import ReservationStatus, UserRole

class ReservationForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=User.objects.filter(role=UserRole.CLIENT),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Client"
    )
    coach = forms.ModelChoiceField(
        queryset=Coach.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Coach",
        required=False
    )
    
    class Meta:
        model = Reservation
        fields = ['client', 'coach', 'date', 'heure', 'statut']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'heure': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'date': 'Date de la réservation',
            'heure': 'Heure de la réservation',
            'statut': 'Statut',
        }

class ClientReservationForm(forms.ModelForm):
    coach = forms.ModelChoiceField(
        queryset=Coach.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Coach",
        required=False
    )
    
    class Meta:
        model = Reservation
        fields = ['coach', 'date', 'heure']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'heure': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
        labels = {
            'date': 'Date de la réservation',
            'heure': 'Heure de la réservation',
        }

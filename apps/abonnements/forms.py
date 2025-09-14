from django import forms
from .models import Abonnement
from apps.users.models import User
from core.enums import UserRole, SubscriptionStatus, SubscriptionType

class AbonnementForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=User.objects.filter(role=UserRole.CLIENT),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Client"
    )

    class Meta:
        model = Abonnement
        fields = ['client', 'type', 'date_debut', 'date_fin', 'statut']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}, choices=SubscriptionType.choices),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'type': 'Type d\'abonnement',
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'statut': 'Statut',
        }

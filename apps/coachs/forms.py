from django import forms
from .models import Coach
from core.enums import CoachSpecialty

class CoachForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Mot de passe",
        required=False,
        help_text="Laissez vide pour ne pas changer le mot de passe"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmer le mot de passe",
        required=False
    )

    class Meta:
        model = Coach
        fields = ['nom', 'email', 'specialite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'specialite': forms.Select(attrs={'class': 'form-select'}, choices=CoachSpecialty.choices),
        }
        labels = {
            'nom': 'Nom complet',
            'email': 'Adresse email',
            'specialite': 'Spécialité',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data

    def save(self, commit=True):
        coach = super().save(commit=False)
        
        # Update password in corresponding User model if provided
        if self.cleaned_data.get('password'):
            try:
                from apps.users.models import User
                user = User.objects.get(email=coach.email)
                user.set_password(self.cleaned_data['password'])
                user.save()
            except User.DoesNotExist:
                pass
        
        if commit:
            coach.save()
        return coach

from django import forms
from .models import User
from core.enums import UserRole, CoachSpecialty

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Mot de passe",
        required=True,
        help_text="Requis pour les nouveaux utilisateurs"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmer le mot de passe",
        required=True
    )

    class Meta:
        model = User
        fields = ['nom', 'email', 'is_active', 'password']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nom': 'Nom complet',
            'email': 'Adresse email',
            'is_active': 'Compte activé',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Validate passwords for UserForm
        if not password:
            self.add_error('password', "Le mot de passe est requis.")
        
        if not password_confirm:
            self.add_error('password_confirm', "La confirmation du mot de passe est requise.")
        
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Les mots de passe ne correspondent pas.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = UserRole.CLIENT  # Always set role to CLIENT for UserForm
        user.is_active = False  # All new users start inactive
        
        # Set password (required for UserForm)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        
        return user

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Mot de passe"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmer le mot de passe"
    )
    specialite = forms.ChoiceField(
        choices=CoachSpecialty.choices,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Spécialité",
        required=False,
        help_text="Requis uniquement pour les coachs"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set role choices to only include CLIENT and COACH
        self.fields['role'].choices = [
            (UserRole.CLIENT, 'Client'),
            (UserRole.COACH, 'Coach')
        ]

    class Meta:
        model = User
        fields = ['nom', 'email', 'role', 'password']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nom': 'Nom complet',
            'email': 'Adresse email',
            'role': 'Type de compte',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        role = cleaned_data.get("role")
        specialite = cleaned_data.get("specialite")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Les mots de passe ne correspondent pas.")
        
        # Validate specialty for coaches
        if role == UserRole.COACH and not specialite:
            self.add_error('specialite', "La spécialité est requise pour les coachs.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # All new users start inactive
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            
            # Create coach record if user is a coach
            if user.role == UserRole.COACH:
                from apps.coachs.models import Coach
                Coach.objects.get_or_create(
                    email=user.email,
                    defaults={
                        'nom': user.nom,
                        'specialite': self.cleaned_data['specialite']
                    }
                )
        
        return user

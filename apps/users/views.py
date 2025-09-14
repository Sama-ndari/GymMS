from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps

from .models import User
from .forms import LoginForm, UserForm, RegistrationForm
from .services import authenticate_user
from apps.sessions.services import create_session
from core.enums import UserRole

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Votre compte a été créé avec succès. Il doit être activé par un administrateur avant de pouvoir vous connecter.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role != UserRole.ADMIN:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def login_view(request):
    if request.user:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            # Check if user exists and password is correct
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    if not user.is_active:
                        messages.error(request, "Votre compte n'a pas encore été activé par un administrateur. Veuillez contacter l'administration.")
                        return render(request, 'users/login.html')
                    
                    # User is active, proceed with login
                    session_key = create_session(user)
                    response = redirect('dashboard')
                    response.set_cookie('session_key', session_key, httponly=True, samesite='Lax')
                    return response
                else:
                    messages.error(request, "L'adresse e-mail ou le mot de passe est incorrect.")
            except User.DoesNotExist:
                messages.error(request, "L'adresse e-mail ou le mot de passe est incorrect.")
        else:
            messages.error(request, "Veuillez remplir tous les champs.")
    
    return render(request, 'users/login.html')

@admin_required
def user_list_view(request):
    users = User.objects.filter(role=UserRole.CLIENT).order_by('is_active', 'date_creation')
    return render(request, 'users/user_list.html', {'users': users})

def password_change_view(request):
    if not request.user:
        return redirect('login')
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Verify current password
        if not request.user.check_password(current_password):
            messages.error(request, 'Mot de passe actuel incorrect.')
            return render(request, 'users/password_change.html')
        
        # Check new password confirmation
        if new_password != confirm_password:
            messages.error(request, 'Les nouveaux mots de passe ne correspondent pas.')
            return render(request, 'users/password_change.html')
        
        # Update password
        request.user.set_password(new_password)
        request.user.save()
        messages.success(request, 'Votre mot de passe a été modifié avec succès.')
        return redirect('dashboard')
    
    return render(request, 'users/password_change.html')

def profile_edit_view(request):
    if not request.user:
        return redirect('login')
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Verify current password
        if not request.user.check_password(current_password):
            messages.error(request, 'Mot de passe actuel incorrect.')
            return render(request, 'users/profile_edit.html')
        
        # Update basic info
        request.user.nom = nom
        request.user.email = email
        
        # Update password if provided
        if new_password:
            if new_password != confirm_password:
                messages.error(request, 'Les nouveaux mots de passe ne correspondent pas.')
                return render(request, 'users/profile_edit.html')
            request.user.set_password(new_password)
        
        request.user.save()
        messages.success(request, 'Votre profil a été mis à jour avec succès.')
        return redirect('dashboard')
    
    return render(request, 'users/profile_edit.html')

@admin_required
def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Le client a été créé avec succès. N'oubliez pas de l'activer.")
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Créer un client'})

@admin_required
def user_update_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "L'utilisateur a été mis à jour avec succès.")
                return redirect('user_list')
            except Exception as e:
                messages.error(request, f"Erreur lors de la mise à jour: {str(e)}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Modifier un utilisateur'})

@admin_required
def user_approve_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
        user.save()
        messages.success(request, f"L'utilisateur {user.nom} a été désactivé.")
    else:
        user.is_active = True
        user.save()
        messages.success(request, f"L'utilisateur {user.nom} a été activé.")
    return redirect('user_list')

@admin_required
def user_delete_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "L'utilisateur a été supprimé avec succès.")
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

# Admin Management Views
@admin_required
def admin_list_view(request):
    """List all administrators in the system"""
    admins = User.objects.filter(role=UserRole.ADMIN).order_by('date_creation')
    return render(request, 'users/admin_list.html', {'admins': admins})

@admin_required
def admin_create_view(request):
    """Create a new administrator account"""
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        is_active = request.POST.get('is_active') == 'on'
        
        # Validation
        if not all([nom, email, password, confirm_password]):
            messages.error(request, "Tous les champs sont obligatoires.")
            return render(request, 'users/admin_form.html')
        
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'users/admin_form.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet email existe déjà.")
            return render(request, 'users/admin_form.html')
        
        # Create admin user
        try:
            admin = User.objects.create_user(
                nom=nom,
                email=email,
                password=password,
                role=UserRole.ADMIN
            )
            # Set activation status after creation
            admin.is_active = is_active
            admin.save()
            messages.success(request, f"L'administrateur {admin.nom} a été créé avec succès.")
            return redirect('admin_list')
        except Exception as e:
            messages.error(request, f"Erreur lors de la création: {str(e)}")
    
    return render(request, 'users/admin_form.html', {'title': 'Créer un administrateur'})

@admin_required
def admin_update_view(request, pk):
    """Update an existing administrator"""
    admin = get_object_or_404(User, pk=pk, role=UserRole.ADMIN)
    
    # Protect superAdmin Samandari from being modified
    if admin.email == 'samandari@gmail.com' and request.user.email != 'samandari@gmail.com':
        messages.error(request, "Seul le super administrateur Samandari peut modifier son propre compte.")
        return redirect('admin_list')
    
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        is_active = request.POST.get('is_active') == 'on'
        
        # Validation
        if not all([nom, email]):
            messages.error(request, "Le nom et l'email sont obligatoires.")
            return render(request, 'users/admin_form.html', {'admin': admin, 'title': 'Modifier un administrateur'})
        
        # Prevent Samandari from changing his email (to maintain protection)
        if admin.email == 'samandari@gmail.com' and email != 'samandari@gmail.com':
            messages.error(request, "L'email du super administrateur ne peut pas être modifié pour des raisons de sécurité.")
            return render(request, 'users/admin_form.html', {'admin': admin, 'title': 'Modifier un administrateur'})
        
        # Check if email is taken by another user
        if User.objects.filter(email=email).exclude(pk=admin.pk).exists():
            messages.error(request, "Un utilisateur avec cet email existe déjà.")
            return render(request, 'users/admin_form.html', {'admin': admin, 'title': 'Modifier un administrateur'})
        
        # Password validation if provided
        if password:
            if password != confirm_password:
                messages.error(request, "Les mots de passe ne correspondent pas.")
                return render(request, 'users/admin_form.html', {'admin': admin, 'title': 'Modifier un administrateur'})
        
        # Update admin
        try:
            admin.nom = nom
            admin.email = email
            admin.is_active = is_active
            
            if password:
                admin.set_password(password)
            
            admin.save()
            messages.success(request, f"L'administrateur {admin.nom} a été mis à jour avec succès.")
            return redirect('admin_list')
        except Exception as e:
            messages.error(request, f"Erreur lors de la mise à jour: {str(e)}")
    
    return render(request, 'users/admin_form.html', {'admin': admin, 'title': 'Modifier un administrateur'})

@admin_required
def admin_toggle_status_view(request, pk):
    """Toggle admin activation status"""
    admin = get_object_or_404(User, pk=pk, role=UserRole.ADMIN)
    
    # Prevent deactivating yourself
    if admin.pk == request.user.pk:
        messages.error(request, "Vous ne pouvez pas désactiver votre propre compte.")
        return redirect('admin_list')
    
    # Protect superAdmin Samandari from being deactivated
    if admin.email == 'samandari@gmail.com':
        messages.error(request, "Le super administrateur Samandari ne peut pas être désactivé.")
        return redirect('admin_list')
    
    admin.is_active = not admin.is_active
    admin.save()
    
    status = "activé" if admin.is_active else "désactivé"
    messages.success(request, f"L'administrateur {admin.nom} a été {status}.")
    return redirect('admin_list')

@admin_required
def admin_delete_view(request, pk):
    """Delete an administrator (with confirmation)"""
    admin = get_object_or_404(User, pk=pk, role=UserRole.ADMIN)
    
    # Prevent deleting yourself
    if admin.pk == request.user.pk:
        messages.error(request, "Vous ne pouvez pas supprimer votre propre compte.")
        return redirect('admin_list')
    
    # Protect superAdmin Samandari from being deleted
    if admin.email == 'samandari@gmail.com':
        messages.error(request, "Le super administrateur Samandari ne peut pas être supprimé.")
        return redirect('admin_list')
    
    # Prevent deleting the last admin
    admin_count = User.objects.filter(role=UserRole.ADMIN, is_active=True).count()
    if admin_count <= 1 and admin.is_active:
        messages.error(request, "Impossible de supprimer le dernier administrateur actif du système.")
        return redirect('admin_list')
    
    if request.method == 'POST':
        admin.delete()
        messages.success(request, f"L'administrateur {admin.nom} a été supprimé avec succès.")
        return redirect('admin_list')
    
    return render(request, 'users/admin_confirm_delete.html', {'admin': admin})

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('session_key')
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return response

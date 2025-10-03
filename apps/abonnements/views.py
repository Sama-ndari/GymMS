from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps

from .models import Abonnement
from .forms import AbonnementForm, ClientAbonnementForm
from apps.users.views import admin_required
from core.enums import UserRole

# Admin views
@admin_required
def abonnement_list_view(request):
    abonnements = Abonnement.objects.all().select_related('client')
    return render(request, 'abonnements/abonnement_list.html', {'abonnements': abonnements})

@admin_required
def abonnement_create_view(request):
    if request.method == 'POST':
        form = AbonnementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'abonnement a été créé avec succès.")
            return redirect('abonnement_list')
    else:
        form = AbonnementForm()
    return render(request, 'abonnements/abonnement_form.html', {'form': form, 'title': 'Créer un abonnement'})

@admin_required
def abonnement_update_view(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    if request.method == 'POST':
        form = AbonnementForm(request.POST, instance=abonnement)
        if form.is_valid():
            form.save()
            messages.success(request, "L'abonnement a été mis à jour avec succès.")
            return redirect('abonnement_list')
    else:
        form = AbonnementForm(instance=abonnement)
    return render(request, 'abonnements/abonnement_form.html', {'form': form, 'title': 'Modifier un abonnement'})

@admin_required
def abonnement_delete_view(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    if request.method == 'POST':
        abonnement.delete()
        messages.success(request, "L'abonnement a été supprimé avec succès.")
        return redirect('abonnement_list')
    return render(request, 'abonnements/abonnement_confirm_delete.html', {'abonnement': abonnement})

# Coach read-only views
def coach_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role not in [UserRole.COACH, UserRole.ADMIN]:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@coach_required
def coach_abonnement_list_view(request):
    abonnements = Abonnement.objects.all().select_related('client')
    return render(request, 'abonnements/coach_abonnement_list.html', {'abonnements': abonnements})

# Client views for own abonnements
def client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role != UserRole.CLIENT:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@client_required
def client_abonnement_list_view(request):
    abonnements = Abonnement.objects.filter(client=request.user)
    return render(request, 'abonnements/client_abonnement_list.html', {'abonnements': abonnements})

@client_required
def client_abonnement_create_view(request):
    """Allow clients to create their own subscriptions"""
    if request.method == 'POST':
        form = ClientAbonnementForm(request.POST)
        if form.is_valid():
            abonnement = form.save(commit=False)
            abonnement.client = request.user  # Set client to current user
            abonnement.save()
            messages.success(request, "Votre abonnement a été créé avec succès.")
            return redirect('client_abonnement_list')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = ClientAbonnementForm()
    
    return render(request, 'abonnements/client_abonnement_form.html', {'form': form, 'title': 'Créer un abonnement'})

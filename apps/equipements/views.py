from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps

from .models import Equipement
from .forms import EquipementForm
from apps.users.views import admin_required
from core.enums import UserRole

# Admin views - full CRUD
@admin_required
def equipement_list_view(request):
    equipements = Equipement.objects.all()
    return render(request, 'equipements/equipement_list.html', {'equipements': equipements})

@admin_required
def equipement_create_view(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'équipement a été créé avec succès.")
            return redirect('equipement_list')
    else:
        form = EquipementForm()
    return render(request, 'equipements/equipement_form.html', {'form': form, 'title': 'Créer un équipement'})

@admin_required
def equipement_update_view(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            messages.success(request, "L'équipement a été mis à jour avec succès.")
            return redirect('equipement_list')
    else:
        form = EquipementForm(instance=equipement)
    return render(request, 'equipements/equipement_form.html', {'form': form, 'title': 'Modifier un équipement'})

@admin_required
def equipement_delete_view(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        equipement.delete()
        messages.success(request, "L'équipement a été supprimé avec succès.")
        return redirect('equipement_list')
    return render(request, 'equipements/equipement_confirm_delete.html', {'equipement': equipement})

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
def coach_equipement_list_view(request):
    equipements = Equipement.objects.all()
    return render(request, 'equipements/coach_equipement_list.html', {'equipements': equipements})

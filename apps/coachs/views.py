from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Coach
from .forms import CoachForm
from apps.users.views import admin_required
from apps.users.models import User
from core.enums import UserRole

@admin_required
def coach_list_view(request):
    coachs = Coach.objects.all()
    # Get corresponding user data for each coach
    coach_data = []
    for coach in coachs:
        try:
            user = User.objects.get(email=coach.email, role=UserRole.COACH)
            coach_data.append({
                'coach': coach,
                'user': user,
                'is_active': user.is_active
            })
        except User.DoesNotExist:
            coach_data.append({
                'coach': coach,
                'user': None,
                'is_active': False
            })
    return render(request, 'coachs/coach_list.html', {'coach_data': coach_data})

@admin_required
def coach_create_view(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le coach a été créé avec succès.")
            return redirect('coach_list')
    else:
        form = CoachForm()
    return render(request, 'coachs/coach_form.html', {'form': form, 'title': 'Créer un coach'})

@admin_required
def coach_update_view(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()
            messages.success(request, "Le coach a été mis à jour avec succès.")
            return redirect('coach_list')
    else:
        form = CoachForm(instance=coach)
    return render(request, 'coachs/coach_form.html', {'form': form, 'title': 'Modifier un coach'})

@admin_required
def coach_delete_view(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    if request.method == 'POST':
        coach.delete()
        messages.success(request, "Le coach a été supprimé avec succès.")
        return redirect('coach_list')
    return render(request, 'coachs/coach_confirm_delete.html', {'coach': coach})

@admin_required
def coach_activate_view(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    try:
        user = User.objects.get(email=coach.email, role=UserRole.COACH)
        if user.is_active:
            user.is_active = False
            user.save()
            messages.success(request, f"Le coach {coach.nom} a été désactivé.")
        else:
            user.is_active = True
            user.save()
            messages.success(request, f"Le coach {coach.nom} a été activé.")
    except User.DoesNotExist:
        messages.error(request, "Aucun compte utilisateur trouvé pour ce coach.")
    return redirect('coach_list')


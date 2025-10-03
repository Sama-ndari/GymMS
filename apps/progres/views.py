from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps

from .models import Progres
from .forms import ProgresForm
from apps.users.views import admin_required
from core.enums import UserRole

# Coach views - full CRUD for progress tracking
def coach_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role not in [UserRole.COACH, UserRole.ADMIN]:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@coach_required
def progres_list_view(request):
    if request.user.role == UserRole.COACH:
        # Get coach instance from user and filter by assigned clients
        try:
            from apps.coachs.models import Coach, CoachClient
            from apps.core.enums import AssignmentStatus
            coach = Coach.objects.get(email=request.user.email)
            # Get only approved assigned clients
            assigned_client_ids = CoachClient.objects.filter(
                coach=coach, 
                actif=True, 
                statut=AssignmentStatus.APPROVED
            ).values_list('client_id', flat=True)
            progres = Progres.objects.filter(coach=coach, client_id__in=assigned_client_ids).select_related('client')
        except Coach.DoesNotExist:
            progres = Progres.objects.none()
            messages.warning(request, "Aucun profil coach trouvé.")
    else:  # Admin
        progres = Progres.objects.all().select_related('client', 'coach')
    
    return render(request, 'progres/progres_list.html', {'progres': progres})

@coach_required
def progres_create_view(request):
    # Admin users should not be able to create progress entries
    if request.user.role == UserRole.ADMIN:
        messages.error(request, "Les administrateurs ne peuvent pas créer de suivi de progrès.")
        return redirect('admin_progres_list')
    
    if request.method == 'POST':
        form = ProgresForm(request.POST)
        # Filter form's client queryset for coaches
        if request.user.role == UserRole.COACH:
            try:
                from apps.coachs.models import Coach, CoachClient
                from apps.core.enums import AssignmentStatus
                coach = Coach.objects.get(email=request.user.email)
                assigned_client_ids = CoachClient.objects.filter(
                    coach=coach, 
                    actif=True, 
                    statut=AssignmentStatus.APPROVED
                ).values_list('client_id', flat=True)
                form.fields['client'].queryset = User.objects.filter(id__in=assigned_client_ids, role=UserRole.CLIENT)
            except Coach.DoesNotExist:
                messages.error(request, "Aucun profil coach trouvé.")
                return redirect('progres_list')
        
        if form.is_valid():
            progres = form.save(commit=False)
            if request.user.role == UserRole.COACH:
                # Get coach instance from user
                try:
                    from apps.coachs.models import Coach
                    coach = Coach.objects.get(email=request.user.email)
                    progres.coach = coach
                except Coach.DoesNotExist:
                    messages.error(request, "Aucun profil coach trouvé.")
                    return redirect('progres_list')
            progres.save()
            messages.success(request, "Le suivi de progrès a été créé avec succès.")
            return redirect('progres_list')
    else:
        form = ProgresForm()
        # Filter form's client queryset for coaches
        if request.user.role == UserRole.COACH:
            try:
                from apps.coachs.models import Coach, CoachClient
                from apps.core.enums import AssignmentStatus
                coach = Coach.objects.get(email=request.user.email)
                assigned_client_ids = CoachClient.objects.filter(
                    coach=coach, 
                    actif=True, 
                    statut=AssignmentStatus.APPROVED
                ).values_list('client_id', flat=True)
                form.fields['client'].queryset = User.objects.filter(id__in=assigned_client_ids, role=UserRole.CLIENT)
            except Coach.DoesNotExist:
                messages.error(request, "Aucun profil coach trouvé.")
                return redirect('progres_list')
    
    return render(request, 'progres/progres_form.html', {'form': form, 'title': 'Nouveau suivi de progrès'})

@coach_required
def progres_update_view(request, pk):
    if request.user.role == UserRole.COACH:
        # Get coach instance from user
        try:
            from apps.coachs.models import Coach
            coach = Coach.objects.get(email=request.user.email)
            progres = get_object_or_404(Progres, pk=pk, coach=coach)
        except Coach.DoesNotExist:
            messages.error(request, "Aucun profil coach trouvé.")
            return redirect('progres_list')
    else:  # Admin
        progres = get_object_or_404(Progres, pk=pk)
    
    if request.method == 'POST':
        form = ProgresForm(request.POST, instance=progres)
        if form.is_valid():
            form.save()
            messages.success(request, "Le suivi de progrès a été mis à jour avec succès.")
            return redirect('progres_list')
    else:
        form = ProgresForm(instance=progres)
    return render(request, 'progres/progres_form.html', {'form': form, 'title': 'Modifier le suivi de progrès'})

@coach_required
def progres_delete_view(request, pk):
    if request.user.role == UserRole.COACH:
        # Get coach instance from user
        try:
            from apps.coachs.models import Coach
            coach = Coach.objects.get(email=request.user.email)
            progres = get_object_or_404(Progres, pk=pk, coach=coach)
        except Coach.DoesNotExist:
            messages.error(request, "Aucun profil coach trouvé.")
            return redirect('progres_list')
    else:  # Admin
        progres = get_object_or_404(Progres, pk=pk)
    
    if request.method == 'POST':
        progres.delete()
        messages.success(request, "Le suivi de progrès a été supprimé avec succès.")
        return redirect('progres_list')
    return render(request, 'progres/progres_confirm_delete.html', {'progres': progres})

# Admin read-only view
@admin_required
def admin_progres_list_view(request):
    progres = Progres.objects.all().select_related('client', 'coach')
    return render(request, 'progres/admin_progres_list.html', {'progres': progres})

# Client views for own progress
def client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role != UserRole.CLIENT:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@client_required
def client_progres_list_view(request):
    progres = Progres.objects.filter(client=request.user).select_related('coach')
    return render(request, 'progres/client_progres_list.html', {'progres': progres})

@client_required
def client_progres_detail_view(request, pk):
    """Client view to see detailed progress including body measurements"""
    progres = get_object_or_404(Progres, pk=pk, client=request.user)
    return render(request, 'progres/progres_detail.html', {'progres': progres, 'is_client': True})

@coach_required
def progres_detail_view(request, pk):
    """Coach/Admin view to see detailed progress including body measurements"""
    if request.user.role == UserRole.COACH:
        try:
            from apps.coachs.models import Coach
            coach = Coach.objects.get(email=request.user.email)
            progres = get_object_or_404(Progres, pk=pk, coach=coach)
        except Coach.DoesNotExist:
            messages.error(request, "Aucun profil coach trouvé.")
            return redirect('progres_list')
    else:  # Admin
        progres = get_object_or_404(Progres, pk=pk)
    
    return render(request, 'progres/progres_detail.html', {'progres': progres, 'is_client': False})

@admin_required
def admin_progres_detail_view(request, pk):
    """Admin detail view for progress with body measurements"""
    progres = get_object_or_404(Progres, pk=pk)
    return render(request, 'progres/progres_detail.html', {'progres': progres, 'is_admin': True})

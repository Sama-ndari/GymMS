from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Reservation
from .forms import ReservationForm, ClientReservationForm
from apps.users.views import admin_required
from core.enums import UserRole

# Admin views - full CRUD
@admin_required
def reservation_list_view(request):
    reservations = Reservation.objects.all().select_related('client', 'coach')
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@admin_required
def reservation_create_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La réservation a été créée avec succès.")
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form, 'title': 'Créer une réservation'})

@admin_required
def reservation_update_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "La réservation a été mise à jour avec succès.")
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_form.html', {'form': form, 'title': 'Modifier une réservation'})

@admin_required
def reservation_delete_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "La réservation a été supprimée avec succès.")
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})

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
def coach_reservation_list_view(request):
    # Get coach instance from user
    try:
        from apps.coachs.models import Coach
        coach = Coach.objects.get(email=request.user.email)
        reservations = Reservation.objects.filter(coach=coach).select_related('client')
    except Coach.DoesNotExist:
        reservations = Reservation.objects.none()
        messages.warning(request, "Aucun profil coach trouvé.")
    
    return render(request, 'reservations/coach_reservation_list.html', {'reservations': reservations})

# Client views for own reservations
def client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role != UserRole.CLIENT:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@client_required
def client_reservation_list_view(request):
    reservations = Reservation.objects.filter(client=request.user).select_related('coach')
    return render(request, 'reservations/client_reservation_list.html', {'reservations': reservations})

@client_required
def client_reservation_create_view(request):
    if request.method == 'POST':
        form = ClientReservationForm(request.POST)
        # Filter coaches to only show approved assignments
        from apps.coachs.models import Coach, CoachClient
        from apps.core.enums import AssignmentStatus
        approved_coach_ids = CoachClient.objects.filter(
            client=request.user,
            actif=True,
            statut=AssignmentStatus.APPROVED
        ).values_list('coach_id', flat=True)
        form.fields['coach'].queryset = Coach.objects.filter(id__in=approved_coach_ids)
        
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            reservation.save()
            messages.success(request, "Votre réservation a été créée avec succès.")
            return redirect('client_reservation_list')
    else:
        form = ClientReservationForm()
        # Filter coaches to only show approved assignments
        from apps.coachs.models import Coach, CoachClient
        from apps.core.enums import AssignmentStatus
        approved_coach_ids = CoachClient.objects.filter(
            client=request.user,
            actif=True,
            statut=AssignmentStatus.APPROVED
        ).values_list('coach_id', flat=True)
        form.fields['coach'].queryset = Coach.objects.filter(id__in=approved_coach_ids)
    
    return render(request, 'reservations/client_reservation_form.html', {'form': form, 'title': 'Nouvelle réservation'})

@client_required
def client_reservation_update_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, client=request.user)
    
    # Check if within edit window (24 hours before)
    reservation_datetime = timezone.make_aware(datetime.combine(reservation.date, reservation.heure))
    edit_window = timedelta(hours=24)
    
    if timezone.now() >= reservation_datetime - edit_window:
        messages.error(request, "Vous ne pouvez plus modifier cette réservation (moins de 24h avant).")
        return redirect('client_reservation_list')
    
    if request.method == 'POST':
        form = ClientReservationForm(request.POST, instance=reservation)
        # Filter coaches to only show approved assignments
        from apps.coachs.models import Coach, CoachClient
        from apps.core.enums import AssignmentStatus
        approved_coach_ids = CoachClient.objects.filter(
            client=request.user,
            actif=True,
            statut=AssignmentStatus.APPROVED
        ).values_list('coach_id', flat=True)
        form.fields['coach'].queryset = Coach.objects.filter(id__in=approved_coach_ids)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été modifiée avec succès.")
            return redirect('client_reservation_list')
    else:
        form = ClientReservationForm(instance=reservation)
        # Filter coaches to only show approved assignments
        from apps.coachs.models import Coach, CoachClient
        from apps.core.enums import AssignmentStatus
        approved_coach_ids = CoachClient.objects.filter(
            client=request.user,
            actif=True,
            statut=AssignmentStatus.APPROVED
        ).values_list('coach_id', flat=True)
        form.fields['coach'].queryset = Coach.objects.filter(id__in=approved_coach_ids)
    
    return render(request, 'reservations/client_reservation_form.html', {'form': form, 'title': 'Modifier ma réservation'})

@client_required
def client_reservation_delete_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, client=request.user)
    
    # Check if within edit window (24 hours before)
    reservation_datetime = timezone.make_aware(datetime.combine(reservation.date, reservation.heure))
    edit_window = timedelta(hours=24)
    
    if timezone.now() >= reservation_datetime - edit_window:
        messages.error(request, "Vous ne pouvez plus annuler cette réservation (moins de 24h avant).")
        return redirect('client_reservation_list')
    
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Votre réservation a été annulée avec succès.")
        return redirect('client_reservation_list')
    return render(request, 'reservations/client_reservation_confirm_delete.html', {'reservation': reservation})

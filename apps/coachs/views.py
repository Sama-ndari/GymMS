from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps
from .models import Coach, CoachClient
from .forms import CoachForm
from apps.users.views import admin_required
from apps.users.models import User
from apps.core.enums import UserRole, AssignmentStatus

# Decorators
def client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role != UserRole.CLIENT:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def coach_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user or request.user.role not in [UserRole.COACH, UserRole.ADMIN]:
            messages.error(request, "Accès non autorisé.")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

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

@admin_required
def coach_clients_view(request):
    """Admin view to see all coach-client assignments"""
    coaches = Coach.objects.all().prefetch_related('coach_clients__client')
    coach_assignments = []
    
    for coach in coaches:
        clients = [cc.client for cc in coach.coach_clients.filter(actif=True)]
        coach_assignments.append({
            'coach': coach,
            'clients': clients,
            'client_count': len(clients)
        })
    
    return render(request, 'coachs/coach_clients.html', {'coach_assignments': coach_assignments})

@admin_required
def assign_client_to_coach_view(request, coach_pk):
    """Assign a client to a coach"""
    coach = get_object_or_404(Coach, pk=coach_pk)
    
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        if client_id:
            try:
                client = User.objects.get(pk=client_id, role=UserRole.CLIENT)
                CoachClient.objects.get_or_create(coach=coach, client=client)
                messages.success(request, f"Le client {client.nom} a été assigné au coach {coach.nom}.")
            except User.DoesNotExist:
                messages.error(request, "Client non trouvé.")
        return redirect('coach_clients')
    
    # Get clients not already assigned to this coach
    assigned_client_ids = CoachClient.objects.filter(coach=coach, actif=True).values_list('client_id', flat=True)
    available_clients = User.objects.filter(role=UserRole.CLIENT, is_active=True).exclude(id__in=assigned_client_ids)
    
    return render(request, 'coachs/assign_client.html', {
        'coach': coach,
        'available_clients': available_clients
    })

@admin_required
def unassign_client_from_coach_view(request, assignment_pk):
    """Remove a client assignment from a coach"""
    assignment = get_object_or_404(CoachClient, pk=assignment_pk)
    
    if request.method == 'POST':
        coach_name = assignment.coach.nom
        client_name = assignment.client.nom
        assignment.actif = False
        assignment.save()
        messages.success(request, f"Le client {client_name} a été retiré du coach {coach_name}.")
        return redirect('coach_clients')
    
    return render(request, 'coachs/unassign_client_confirm.html', {'assignment': assignment})

# ===============================
# CLIENT VIEWS - Coach Requests
# ===============================

@client_required
def client_my_coaches_view(request):
    """Client view to see their coaches and requests"""
    # Get all coach assignments for this client
    assignments = CoachClient.objects.filter(
        client=request.user,
        actif=True
    ).select_related('coach').order_by('-date_assignation')
    
    # Separate by status
    approved_coaches = assignments.filter(statut=AssignmentStatus.APPROVED)
    pending_requests = assignments.filter(statut=AssignmentStatus.PENDING)
    
    # Get available coaches (not already requested)
    requested_coach_ids = assignments.values_list('coach_id', flat=True)
    available_coaches = Coach.objects.exclude(id__in=requested_coach_ids)
    
    return render(request, 'coachs/client_my_coaches.html', {
        'approved_coaches': approved_coaches,
        'pending_requests': pending_requests,
        'available_coaches': available_coaches
    })

@client_required
def client_request_coach_view(request, coach_pk):
    """Client requests to be assigned to a coach"""
    coach = get_object_or_404(Coach, pk=coach_pk)
    
    # Check if already requested
    existing = CoachClient.objects.filter(coach=coach, client=request.user, actif=True).first()
    if existing:
        messages.warning(request, f"Vous avez déjà une demande {'en attente' if existing.statut == AssignmentStatus.PENDING else 'approuvée'} pour ce coach.")
        return redirect('client_my_coaches')
    
    # Create pending request
    CoachClient.objects.create(
        coach=coach,
        client=request.user,
        statut=AssignmentStatus.PENDING
    )
    messages.success(request, f"Votre demande d'assignation au coach {coach.nom} a été envoyée.")
    return redirect('client_my_coaches')

@client_required
def client_cancel_request_view(request, assignment_pk):
    """Client cancels their coach request"""
    assignment = get_object_or_404(CoachClient, pk=assignment_pk, client=request.user)
    
    if request.method == 'POST':
        coach_name = assignment.coach.nom
        assignment.actif = False
        assignment.save()
        messages.success(request, f"Votre demande au coach {coach_name} a été annulée.")
        return redirect('client_my_coaches')
    
    return render(request, 'coachs/client_cancel_request.html', {'assignment': assignment})

# ===============================
# COACH VIEWS - Client Management
# ===============================

@coach_required
def coach_my_clients_view(request):
    """Coach view to see their clients and pending requests"""
    try:
        coach = Coach.objects.get(email=request.user.email)
    except Coach.DoesNotExist:
        messages.error(request, "Aucun profil coach trouvé.")
        return redirect('dashboard')
    
    # Get all assignments
    assignments = CoachClient.objects.filter(
        coach=coach,
        actif=True
    ).select_related('client').order_by('-date_assignation')
    
    # Separate by status
    approved_clients = assignments.filter(statut=AssignmentStatus.APPROVED)
    pending_requests = assignments.filter(statut=AssignmentStatus.PENDING)
    
    return render(request, 'coachs/coach_my_clients.html', {
        'approved_clients': approved_clients,
        'pending_requests': pending_requests,
        'coach': coach
    })

@coach_required
def coach_approve_request_view(request, assignment_pk):
    """Coach approves a client request"""
    try:
        coach = Coach.objects.get(email=request.user.email)
    except Coach.DoesNotExist:
        messages.error(request, "Aucun profil coach trouvé.")
        return redirect('dashboard')
    
    assignment = get_object_or_404(CoachClient, pk=assignment_pk, coach=coach, statut=AssignmentStatus.PENDING)
    assignment.statut = AssignmentStatus.APPROVED
    assignment.save()
    messages.success(request, f"Vous avez approuvé la demande de {assignment.client.nom}.")
    return redirect('coach_my_clients')

@coach_required
def coach_reject_request_view(request, assignment_pk):
    """Coach rejects a client request"""
    try:
        coach = Coach.objects.get(email=request.user.email)
    except Coach.DoesNotExist:
        messages.error(request, "Aucun profil coach trouvé.")
        return redirect('dashboard')
    
    assignment = get_object_or_404(CoachClient, pk=assignment_pk, coach=coach, statut=AssignmentStatus.PENDING)
    assignment.statut = AssignmentStatus.REJECTED
    assignment.actif = False
    assignment.save()
    messages.success(request, f"Vous avez refusé la demande de {assignment.client.nom}.")
    return redirect('coach_my_clients')

@coach_required
def coach_deassign_client_view(request, assignment_pk):
    """Coach removes a client from their list"""
    try:
        coach = Coach.objects.get(email=request.user.email)
    except Coach.DoesNotExist:
        messages.error(request, "Aucun profil coach trouvé.")
        return redirect('dashboard')
    
    assignment = get_object_or_404(CoachClient, pk=assignment_pk, coach=coach, statut=AssignmentStatus.APPROVED)
    
    if request.method == 'POST':
        client_name = assignment.client.nom
        assignment.actif = False
        assignment.save()
        messages.success(request, f"Le client {client_name} a été retiré de votre liste.")
        return redirect('coach_my_clients')
    
    return render(request, 'coachs/coach_deassign_client.html', {'assignment': assignment})


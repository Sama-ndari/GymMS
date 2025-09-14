from django.shortcuts import render, redirect
from apps.users.models import User
from apps.equipements.models import Equipement
from apps.coachs.models import Coach
from core.enums import UserRole

def welcome_view(request):
    """Landing page: if logged in, go to dashboard; else show welcome."""
    if request.user and hasattr(request.user, 'is_authenticated') and request.user.is_authenticated:
        return redirect('dashboard')
    
    # Get real statistics from database
    stats = {
        'active_members': User.objects.filter(is_active=True, role=UserRole.CLIENT).count(),
        'total_equipment': Equipement.objects.count(),
        'expert_coaches': Coach.objects.count(),
        'satisfaction_rate': 98  # This could be calculated from feedback/reviews if available
    }
    
    return render(request, 'core/welcome.html', {'stats': stats})

def dashboard_view(request):
    if not request.user:
        return redirect('login')
    
    context = {
        'user': request.user
    }
    return render(request, 'core/dashboard.html', context)

# Information pages
def histoire_view(request):
    return render(request, 'core/histoire.html')

def equipe_view(request):
    return render(request, 'core/equipe.html')

def carrieres_view(request):
    return render(request, 'core/carrieres.html')

def confidentialite_view(request):
    return render(request, 'core/confidentialite.html')


from django.core.management.base import BaseCommand
from apps.reservations.models import Reservation
from apps.users.models import User
from apps.coachs.models import Coach
from core.enums import ReservationStatus, UserRole
from datetime import date, time, timedelta

class Command(BaseCommand):
    help = 'Load sample reservation data'

    def handle(self, *args, **options):
        # Clear existing reservations
        Reservation.objects.all().delete()
        
        # Get existing clients and coaches
        clients = User.objects.filter(role=UserRole.CLIENT)
        coaches = Coach.objects.all()
        
        if not clients.exists():
            self.stdout.write(self.style.WARNING('No clients found. Run load_sample_abonnements first.'))
            return
            
        if not coaches.exists():
            self.stdout.write(self.style.WARNING('No coaches found. Run load_sample_coaches first.'))
            return
        
        # Sample reservation data
        today = date.today()
        reservations_data = [
            {
                'client': clients[0],
                'coach': coaches[0],
                'date': today + timedelta(days=1),
                'heure': time(9, 0),
                'statut': ReservationStatus.PLANNED
            },
            {
                'client': clients[1],
                'coach': coaches[1],
                'date': today + timedelta(days=2),
                'heure': time(10, 30),
                'statut': ReservationStatus.PLANNED
            },
            {
                'client': clients[2],
                'coach': coaches[0],
                'date': today + timedelta(days=3),
                'heure': time(14, 0),
                'statut': ReservationStatus.PLANNED
            },
            {
                'client': clients[0],
                'coach': coaches[2],
                'date': today - timedelta(days=1),
                'heure': time(16, 0),
                'statut': ReservationStatus.COMPLETED
            },
            {
                'client': clients[3],
                'coach': coaches[1],
                'date': today - timedelta(days=2),
                'heure': time(11, 0),
                'statut': ReservationStatus.CANCELLED
            },
            {
                'client': clients[1],
                'coach': coaches[3],
                'date': today + timedelta(days=5),
                'heure': time(8, 30),
                'statut': ReservationStatus.PLANNED
            },
            {
                'client': clients[2],
                'coach': None,  # No coach assigned
                'date': today + timedelta(days=4),
                'heure': time(15, 30),
                'statut': ReservationStatus.PLANNED
            }
        ]
        
        # Create reservation objects
        for data in reservations_data:
            Reservation.objects.create(**data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(reservations_data)} reservations')
        )

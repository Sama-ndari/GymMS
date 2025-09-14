from django.core.management.base import BaseCommand
from apps.progres.models import Progres
from apps.users.models import User
from apps.coachs.models import Coach
from core.enums import UserRole
from datetime import date, timedelta
import json

class Command(BaseCommand):
    help = 'Load sample progress data'

    def handle(self, *args, **options):
        # Clear existing progress
        Progres.objects.all().delete()
        
        # Get existing clients and coaches
        clients = User.objects.filter(role=UserRole.CLIENT)
        coaches = Coach.objects.all()
        
        if not clients.exists():
            self.stdout.write(self.style.WARNING('No clients found. Run load_sample_abonnements first.'))
            return
            
        if not coaches.exists():
            self.stdout.write(self.style.WARNING('No coaches found. Run load_sample_coaches first.'))
            return
        
        # Sample progress data
        today = date.today()
        progres_data = [
            {
                'client': clients[0],
                'coach': coaches[0],
                'date': today - timedelta(days=30),
                'notes': 'Première séance d\'évaluation. Bon niveau de base, motivation élevée.',
                'poids': 75.5,
                'mesures': json.dumps({'chest': 95, 'waist': 82, 'biceps': 35})
            },
            {
                'client': clients[0],
                'coach': coaches[0],
                'date': today - timedelta(days=15),
                'notes': 'Progression notable en force. Augmentation des charges sur tous les exercices.',
                'poids': 74.8,
                'mesures': json.dumps({'chest': 96, 'waist': 81, 'biceps': 36})
            },
            {
                'client': clients[0],
                'coach': coaches[0],
                'date': today - timedelta(days=7),
                'notes': 'Excellente forme physique. Technique parfaite sur les mouvements complexes.',
                'poids': 74.2,
                'mesures': json.dumps({'chest': 97, 'waist': 80, 'biceps': 36.5})
            },
            {
                'client': clients[1],
                'coach': coaches[1],
                'date': today - timedelta(days=20),
                'notes': 'Début du programme cardio. Objectif: améliorer l\'endurance cardiovasculaire.',
                'poids': 68.0,
                'mesures': json.dumps({'chest': 88, 'waist': 75, 'thighs': 58})
            },
            {
                'client': clients[1],
                'coach': coaches[1],
                'date': today - timedelta(days=10),
                'notes': 'Amélioration significative de l\'endurance. Peut maintenir un rythme plus élevé.',
                'poids': 67.3,
                'mesures': json.dumps({'chest': 89, 'waist': 74, 'thighs': 59})
            },
            {
                'client': clients[2],
                'coach': coaches[2],
                'date': today - timedelta(days=25),
                'notes': 'Initiation au yoga. Travail sur la flexibilité et l\'équilibre.',
                'poids': 62.5,
                'mesures': json.dumps({'flexibility_score': 6, 'balance_score': 7})
            },
            {
                'client': clients[2],
                'coach': coaches[2],
                'date': today - timedelta(days=12),
                'notes': 'Progrès remarquables en flexibilité. Postures plus stables et maintenues plus longtemps.',
                'poids': 62.8,
                'mesures': json.dumps({'flexibility_score': 8, 'balance_score': 8})
            }
        ]
        
        # Create progress objects
        for data in progres_data:
            Progres.objects.create(**data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(progres_data)} progress entries')
        )

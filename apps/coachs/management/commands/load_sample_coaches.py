from django.core.management.base import BaseCommand
from apps.coachs.models import Coach

class Command(BaseCommand):
    help = 'Load sample coach data'

    def handle(self, *args, **options):
        # Clear existing coaches
        Coach.objects.all().delete()
        
        # Sample coach data
        coaches_data = [
            {
                'nom': 'Coach1',
                'email': 'coach1@gmail.com',
                'password': 'coach123',
                'specialite': 'Musculation et Force'
            },
            {
                'nom': 'Marie Dubois',
                'email': 'marie.dubois@gymms.com',
                'password': 'marie123',
                'specialite': 'Cardio et Endurance'
            },
            {
                'nom': 'Pierre Martin',
                'email': 'pierre.martin@gymms.com',
                'password': 'pierre123',
                'specialite': 'Yoga et Pilates'
            },
            {
                'nom': 'Sophie Laurent',
                'email': 'sophie.laurent@gymms.com',
                'password': 'sophie123',
                'specialite': 'CrossFit et HIIT'
            },
            {
                'nom': 'Thomas Bernard',
                'email': 'thomas.bernard@gymms.com',
                'password': 'thomas123',
                'specialite': 'Préparation physique'
            }
        ]
        
        # Create coach objects
        for data in coaches_data:
            Coach.objects.create(
                nom=data['nom'],
                email=data['email'],
                specialite=data['specialite']
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(coaches_data)} coaches')
        )

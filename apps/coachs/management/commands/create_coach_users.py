from django.core.management.base import BaseCommand
from apps.users.models import User
from apps.coachs.models import Coach
from core.enums import UserRole

class Command(BaseCommand):
    help = 'Create User accounts for existing coaches'

    def handle(self, *args, **options):
        coaches = Coach.objects.all()
        
        for coach in coaches:
            # Check if user already exists
            if not User.objects.filter(email=coach.email).exists():
                user = User.objects.create(
                    nom=coach.nom,
                    email=coach.email,
                    role=UserRole.COACH
                )
                # Set default password based on coach name
                if 'Coach1' in coach.nom:
                    password = 'coach123'
                elif 'Marie' in coach.nom:
                    password = 'marie123'
                elif 'Pierre' in coach.nom:
                    password = 'pierre123'
                elif 'Sophie' in coach.nom:
                    password = 'sophie123'
                elif 'Thomas' in coach.nom:
                    password = 'thomas123'
                else:
                    password = 'default123'
                
                user.set_password(password)
                user.save()
                
                self.stdout.write(
                    self.style.SUCCESS(f'Created user for coach: {coach.nom}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'User already exists for: {coach.nom}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Coach user creation completed')
        )

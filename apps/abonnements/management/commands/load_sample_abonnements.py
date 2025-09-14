from django.core.management.base import BaseCommand
from apps.abonnements.models import Abonnement
from apps.users.models import User
from core.enums import SubscriptionStatus, UserRole
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Load sample abonnement data'

    def handle(self, *args, **options):
        # Clear existing abonnements
        Abonnement.objects.all().delete()
        
        # Create some sample clients first
        User.objects.filter(role=UserRole.CLIENT).delete()
        
        clients_data = [
            {'nom': 'Client Test', 'email': 'client@gmail.com', 'password': 'client123'},
            {'nom': 'Jean Dupont', 'email': 'jean.dupont@email.com', 'password': 'jean123'},
            {'nom': 'Alice Martin', 'email': 'alice.martin@email.com', 'password': 'alice123'},
            {'nom': 'Bob Wilson', 'email': 'bob.wilson@email.com', 'password': 'bob123'},
            {'nom': 'Emma Garcia', 'email': 'emma.garcia@email.com', 'password': 'emma123'},
        ]
        
        clients = []
        for data in clients_data:
            client = User.objects.create(
                nom=data['nom'],
                email=data['email'],
                role=UserRole.CLIENT
            )
            client.set_password(data['password'])
            client.save()
            clients.append(client)
        
        # Sample abonnement data
        today = date.today()
        abonnements_data = [
            {
                'client': clients[0],
                'type': 'Mensuel Standard',
                'date_debut': today - timedelta(days=15),
                'date_fin': today + timedelta(days=15),
                'statut': SubscriptionStatus.ACTIVE
            },
            {
                'client': clients[1],
                'type': 'Annuel Premium',
                'date_debut': today - timedelta(days=60),
                'date_fin': today + timedelta(days=305),
                'statut': SubscriptionStatus.ACTIVE
            },
            {
                'client': clients[2],
                'type': 'Trimestriel',
                'date_debut': today - timedelta(days=30),
                'date_fin': today + timedelta(days=60),
                'statut': SubscriptionStatus.ACTIVE
            },
            {
                'client': clients[3],
                'type': 'Mensuel Standard',
                'date_debut': today - timedelta(days=45),
                'date_fin': today - timedelta(days=15),
                'statut': SubscriptionStatus.EXPIRED
            },
            {
                'client': clients[4],
                'type': 'Hebdomadaire',
                'date_debut': today + timedelta(days=5),
                'date_fin': today + timedelta(days=12),
                'statut': SubscriptionStatus.ACTIVE
            }
        ]
        
        # Create abonnement objects
        for data in abonnements_data:
            Abonnement.objects.create(**data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(clients)} clients and {len(abonnements_data)} abonnements')
        )

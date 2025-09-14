from django.core.management.base import BaseCommand
from apps.equipements.models import Equipement
from core.enums import EquipmentStatus

class Command(BaseCommand):
    help = 'Load sample equipment data'

    def handle(self, *args, **options):
        # Clear existing equipment
        Equipement.objects.all().delete()
        
        # Sample equipment data
        equipment_data = [
            {'nom': 'Tapis de course', 'type': 'Cardio', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Vélo stationnaire', 'type': 'Cardio', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Rameur Concept2', 'type': 'Cardio', 'statut': EquipmentStatus.MAINTENANCE},
            {'nom': 'Banc plat', 'type': 'Poids libres', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Haltères 10kg', 'type': 'Poids libres', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Barre olympique', 'type': 'Poids libres', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Presse à cuisses', 'type': 'Musculation guidée', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Poulie vis-à-vis', 'type': 'Musculation guidée', 'statut': EquipmentStatus.MAINTENANCE},
            {'nom': 'Kettlebell 16kg', 'type': 'Accessoires', 'statut': EquipmentStatus.AVAILABLE},
            {'nom': 'Corde à sauter', 'type': 'Accessoires', 'statut': EquipmentStatus.AVAILABLE},
        ]
        
        # Create equipment objects
        for data in equipment_data:
            Equipement.objects.create(**data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(equipment_data)} equipment items')
        )

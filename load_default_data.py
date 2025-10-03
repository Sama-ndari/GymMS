#!/usr/bin/env python
"""
Resets the database and loads a set of default data for testing.
WARNING: This script will DELETE ALL DATA in the database.
"""
import os
import django
from datetime import date, timedelta, time

def setup_django():
    """Sets up the Django environment to allow script to run outside of manage.py"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymms.settings')
    django.setup()

setup_django()

from django.core.management import call_command
from apps.users.models import User
from apps.coachs.models import Coach, CoachClient
from apps.abonnements.models import Abonnement
from apps.reservations.models import Reservation
from apps.progres.models import Progres
from apps.equipements.models import Equipement
from core.enums import UserRole, AssignmentStatus, EquipmentStatus, EquipmentType, ReservationStatus, SubscriptionStatus, SubscriptionType, CoachSpecialty

def clear_database():
    """
    Clears all data from the database using Django's flush command.
    Prompts the user for confirmation before proceeding.
    """
    print("\n⚠️  WARNING: This will delete ALL data from the database, including user accounts.")
    confirm = input("    Are you sure you want to proceed? (yes/no): ")
    if confirm.lower() == 'yes':
        print("\nFlushing the database...")
        call_command('flush', '--no-input')
        print("✅ Database has been cleared.")
        return True
    else:
        print("\n❌ Operation cancelled by user.")
        return False

def create_data():
    """
    Populates the database with a default set of users, coaches, clients,
    and other related data for testing purposes.
    """
    print("\n➕ Creating default data set...")

    # 1. Create Admins
    print("\n--- Creating Admins ---")
    admin_sam = User.objects.create_superuser('samandari@gmail.com', 'sam123', nom='Samandari')
    admin_gdbb = User.objects.create_user('gdbb@gmail.com', 'gdbb123', nom='GrandBB', role=UserRole.ADMIN)
    admin_gdbb.is_active = True
    admin_gdbb.save()
    admins = {'samandari': admin_sam, 'gdbb': admin_gdbb}
    for name, admin in admins.items():
        print(f"  ✓ Created admin: {name} ({admin.email})")

    # 2. Create Coaches (User and Coach models)
    print("\n--- Creating Coaches ---")
    coaches_data = [
        {'email': 'marie.dubois@gymms.com', 'password': 'marie123', 'nom': 'Marie Dubois', 'specialite': CoachSpecialty.CARDIO_ENDURANCE},
        {'email': 'pierre.martin@gymms.com', 'password': 'pierre123', 'nom': 'Pierre Martin', 'specialite': CoachSpecialty.YOGA_PILATES},
        {'email': 'sophie.laurent@gymms.com', 'password': 'sophie123', 'nom': 'Sophie Laurent', 'specialite': CoachSpecialty.CROSSFIT_HIIT},
        {'email': 'thomas.bernard@gymms.com', 'password': 'thomas123', 'nom': 'Thomas Bernard', 'specialite': CoachSpecialty.PREPARATION_PHYSIQUE},
    ]
    coaches = {}
    for data in coaches_data:
        user = User.objects.create_user(email=data['email'], password=data['password'], nom=data['nom'], role=UserRole.COACH)
        user.is_active = True
        user.save()
        coach = Coach.objects.create(nom=data['nom'], email=data['email'], specialite=data['specialite'])
        coaches[data['nom']] = coach
        print(f"  ✓ Created coach: {user.nom} ({user.email})")

    # 3. Create Clients
    print("\n--- Creating Clients ---")
    clients_data = [
        {'email': 'jean.dupont@email.com', 'password': 'jean123', 'nom': 'Jean Dupont'},
        {'email': 'alice.martin@email.com', 'password': 'alice123', 'nom': 'Alice Martin'},
        {'email': 'bob.wilson@email.com', 'password': 'bob123', 'nom': 'Bob Wilson'},
        {'email': 'emma.garcia@email.com', 'password': 'emma123', 'nom': 'Emma Garcia'},
    ]
    clients = {}
    for data in clients_data:
        user = User.objects.create_user(email=data['email'], password=data['password'], nom=data['nom'], role=UserRole.CLIENT)
        user.is_active = True
        user.save()
        clients[data['nom']] = user
        print(f"  ✓ Created client: {user.nom} ({user.email})")

    # 4. Create Coach-Client Assignments
    print("\n--- Creating Assignments (All Approved) ---")
    assignments = [
        {'coach': coaches['Marie Dubois'], 'client': clients['Jean Dupont']},
        {'coach': coaches['Marie Dubois'], 'client': clients['Alice Martin']},
        {'coach': coaches['Pierre Martin'], 'client': clients['Bob Wilson']},
        {'coach': coaches['Sophie Laurent'], 'client': clients['Emma Garcia']},
        {'coach': coaches['Thomas Bernard'], 'client': clients['Jean Dupont']},
    ]
    for assign in assignments:
        CoachClient.objects.create(coach=assign['coach'], client=assign['client'], statut=AssignmentStatus.APPROVED, actif=True)
        print(f"  ✓ Assigned {assign['client'].nom} to {assign['coach'].nom}")

    # 5. Create Subscriptions for Clients
    print("\n--- Creating Subscriptions ---")
    Abonnement.objects.create(client=clients['Jean Dupont'], type=SubscriptionType.MENSUEL_STANDARD, date_debut=date(2025, 10, 3), date_fin=date(2025, 10, 24), statut=SubscriptionStatus.ACTIVE)
    Abonnement.objects.create(client=clients['Alice Martin'], type=SubscriptionType.TRIMESTRIEL, date_debut=date(2025, 8, 8), date_fin=date(2025, 11, 6), statut=SubscriptionStatus.ACTIVE)
    Abonnement.objects.create(client=clients['Bob Wilson'], type=SubscriptionType.MENSUEL_STANDARD, date_debut=date(2025, 7, 24), date_fin=date(2025, 8, 23), statut=SubscriptionStatus.EXPIRED)
    Abonnement.objects.create(client=clients['Emma Garcia'], type=SubscriptionType.HEBDOMADAIRE, date_debut=date(2025, 9, 12), date_fin=date(2025, 9, 19), statut=SubscriptionStatus.ACTIVE)
    print("  ✓ Created sample subscriptions for all clients.")

    # 6. Create Equipment
    print("\n--- Creating Equipment ---")
    equipment_data = [
        {'nom': 'Tapis de course', 'type': EquipmentType.CARDIO, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Vélo stationnaire', 'type': EquipmentType.CARDIO, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Rameur Concept2', 'type': EquipmentType.CARDIO, 'statut': EquipmentStatus.MAINTENANCE},
        {'nom': 'Banc plat', 'type': EquipmentType.POIDS_LIBRES, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Haltères 10kg', 'type': EquipmentType.POIDS_LIBRES, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Barre olympique', 'type': EquipmentType.POIDS_LIBRES, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Presse à cuisses', 'type': EquipmentType.MUSCULATION_GUIDEE, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Poulie vis-à-vis', 'type': EquipmentType.MUSCULATION_GUIDEE, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Kettlebell 16kg', 'type': EquipmentType.ACCESSOIRES, 'statut': EquipmentStatus.AVAILABLE},
        {'nom': 'Corde à sauter', 'type': EquipmentType.ACCESSOIRES, 'statut': EquipmentStatus.AVAILABLE},
    ]
    for equip in equipment_data:
        Equipement.objects.create(**equip)
    print(f"  ✓ Created {len(equipment_data)} pieces of equipment.")

    # 7. Create Reservations
    print("\n--- Creating Reservations ---")
    Reservation.objects.create(client=clients['Jean Dupont'], coach=coaches['Marie Dubois'], date=date(2025, 10, 6), heure=time(12, 0), statut=ReservationStatus.PLANNED)
    Reservation.objects.create(client=clients['Alice Martin'], coach=coaches['Marie Dubois'], date=date(2025, 9, 9), heure=time(12, 0), statut=ReservationStatus.PLANNED)
    Reservation.objects.create(client=clients['Bob Wilson'], coach=coaches['Pierre Martin'], date=date(2025, 9, 19), heure=time(8, 30), statut=ReservationStatus.PLANNED)
    print("  ✓ Created sample reservations.")

    # 8. Create Progress entries
    print("\n--- Creating Progress Entries ---")
    Progres.objects.create(
        client=clients['Jean Dupont'], coach=coaches['Marie Dubois'], date=date(2025, 9, 26), poids=85.50,
        mesures={'poitrine': 105, 'taille': 90, 'hanches': 98, 'bras_gauche': 38, 'bras_droit': 38, 'cuisse_gauche': 58, 'cuisse_droite': 58, 'mollet_gauche': 38, 'mollet_droit': 38, 'masse_grasse': 18.5},
        notes='Excellent progrès ! Continue comme ça. Poids en baisse, muscles en hausse.'
    )
    Progres.objects.create(
        client=clients['Alice Martin'], coach=coaches['Marie Dubois'], date=date(2025, 9, 28), poids=62.30,
        mesures={'poitrine': 88, 'taille': 68, 'hanches': 92, 'bras_gauche': 28, 'bras_droit': 28, 'cuisse_gauche': 52, 'cuisse_droite': 52, 'mollet_gauche': 34, 'mollet_droit': 34, 'masse_grasse': 22.0},
        notes='Bonne progression en cardio. Continuez les exercices de renforcement musculaire.'
    )
    Progres.objects.create(
        client=clients['Bob Wilson'], coach=coaches['Pierre Martin'], date=date(2025, 10, 3), poids=78.50,
        mesures={'poitrine': 98, 'taille': 85, 'hanches': 95, 'bras_gauche': 35, 'bras_droit': 35, 'cuisse_gauche': 55, 'cuisse_droite': 55, 'mollet_gauche': 36, 'mollet_droit': 36, 'masse_grasse': 16.0},
        notes='Bon début! Focus sur la flexibilité avec le yoga.'
    )
    print("  ✓ Created sample progress entries.")

    print("\n✨ Default data loading complete! ✨")

if __name__ == "__main__":
    if clear_database():
        create_data()

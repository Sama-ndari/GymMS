from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    COACH = 'COACH', 'Coach'
    CLIENT = 'CLIENT', 'Client'

class SubscriptionStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Actif'
    EXPIRED = 'EXPIRED', 'Expiré'
    CANCELLED = 'CANCELLED', 'Annulé'

class SubscriptionType(models.TextChoices):
    MENSUEL_STANDARD = 'Mensuel Standard', 'Mensuel Standard'
    TRIMESTRIEL = 'Trimestriel', 'Trimestriel'
    SEMESTRIEL = 'Semestriel', 'Semestriel'
    HEBDOMADAIRE = 'Hebdomadaire', 'Hebdomadaire'
    ANNUEL_PREMIUM = 'Annuel Premium', 'Annuel Premium'
    PASS_JOURNEE = 'Pass journée', 'Pass journée'
    PASS_10_SEANCES = 'Pass 10 séances', 'Pass 10 séances'
    VIP = 'VIP', 'VIP'

class EquipmentStatus(models.TextChoices):
    AVAILABLE = 'DISPONIBLE', 'Disponible'
    MAINTENANCE = 'MAINTENANCE', 'En maintenance'

class EquipmentType(models.TextChoices):
    CARDIO = 'Cardio', 'Cardio'
    MUSCULATION_GUIDEE = 'Musculation guidée', 'Musculation guidée'
    POIDS_LIBRES = 'Poids libres', 'Poids libres'
    ACCESSOIRES = 'Accessoires', 'Accessoires'

class CoachSpecialty(models.TextChoices):
    MUSCULATION_FORCE = 'Musculation et Force', 'Musculation et Force'
    CARDIO_ENDURANCE = 'Cardio et Endurance', 'Cardio et Endurance'
    YOGA_PILATES = 'Yoga et Pilates', 'Yoga et Pilates'
    CROSSFIT_HIIT = 'CrossFit et HIIT', 'CrossFit et HIIT'
    PREPARATION_PHYSIQUE = 'Préparation physique', 'Préparation physique'
    NUTRITION_WELLNESS = 'Nutrition et Bien-être', 'Nutrition et Bien-être'
    REHABILITATION = 'Rééducation', 'Rééducation'
    SPORTS_SPECIFIQUES = 'Sports spécifiques', 'Sports spécifiques'

class ReservationStatus(models.TextChoices):
    PLANNED = 'PLANIFIEE', 'Planifiée'
    COMPLETED = 'TERMINEE', 'Terminée'
    CANCELLED = 'ANNULEE', 'Annulée'

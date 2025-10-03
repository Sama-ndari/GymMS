from django.db import models
from apps.core.enums import CoachSpecialty, AssignmentStatus

class Coach(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialite = models.CharField(max_length=50, choices=CoachSpecialty.choices, default=CoachSpecialty.MUSCULATION_FORCE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.specialite}"

    class Meta:
        app_label = 'coachs'
        verbose_name = "Coach"
        verbose_name_plural = "Coachs"
        ordering = ['nom']

class CoachClient(models.Model):
    """Model to track coach-client relationships with approval workflow"""
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='coach_clients')
    client = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='client_coaches', limit_choices_to={'role': 'CLIENT'})
    date_assignation = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)
    statut = models.CharField(
        max_length=20,
        choices=AssignmentStatus.choices,
        default=AssignmentStatus.PENDING,
        help_text="Statut de la demande d'assignation"
    )

    def __str__(self):
        return f"{self.coach.nom} - {self.client.nom} ({self.get_statut_display()})"

    class Meta:
        verbose_name = "Assignation Coach-Client"
        verbose_name_plural = "Assignations Coach-Client"
        ordering = ['-date_assignation']
        unique_together = ('coach', 'client')

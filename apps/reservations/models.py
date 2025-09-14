from django.db import models
from django.conf import settings
from core.enums import ReservationStatus

class Reservation(models.Model):
    client = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        related_name='reservations',
        limit_choices_to={'role': 'CLIENT'}
    )
    coach = models.ForeignKey(
        'coachs.Coach', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='reservations'
    )
    date = models.DateField()
    heure = models.TimeField()
    statut = models.CharField(
        max_length=20,
        choices=ReservationStatus.choices,
        default=ReservationStatus.PLANNED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        coach_nom = self.coach.nom if self.coach else 'Non assigné'
        return f"Réservation pour {self.client.nom} avec {coach_nom} le {self.date} à {self.heure}"

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
        ordering = ['date', 'heure']
        unique_together = ('coach', 'date', 'heure')

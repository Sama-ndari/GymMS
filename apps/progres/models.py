from django.db import models
from django.conf import settings

class Progres(models.Model):
    client = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        related_name='progres',
        limit_choices_to={'role': 'CLIENT'}
    )
    coach = models.ForeignKey(
        'coachs.Coach', 
        on_delete=models.CASCADE, 
        related_name='progres_suivis'
    )
    date = models.DateField()
    notes = models.TextField()
    poids = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mesures = models.JSONField(null=True, blank=True)  # e.g., {'chest': 98, 'waist': 80}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Suivi de progrès pour {self.client.nom} par {self.coach.nom} le {self.date}"

    class Meta:
        verbose_name = "Progrès"
        verbose_name_plural = "Progrès"
        ordering = ['-date']

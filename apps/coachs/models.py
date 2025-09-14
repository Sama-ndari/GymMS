from django.db import models
from core.enums import CoachSpecialty

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

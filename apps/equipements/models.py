from django.db import models
from apps.coachs.models import Coach
from core.enums import EquipmentStatus, EquipmentType

class Equipement(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=EquipmentType.choices, default=EquipmentType.CARDIO)
    statut = models.CharField(max_length=20, choices=EquipmentStatus.choices, default=EquipmentStatus.AVAILABLE)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipements')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.type})"

    class Meta:
        app_label = 'equipements'
        verbose_name = "Équipement"
        verbose_name_plural = "Équipements"
        ordering = ['nom']

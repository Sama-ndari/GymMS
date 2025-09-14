from django.db import models
from apps.users.models import User
from core.enums import SubscriptionStatus, SubscriptionType

class Abonnement(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abonnements')
    type = models.CharField(max_length=50, choices=SubscriptionType.choices, default=SubscriptionType.MENSUEL_STANDARD)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=SubscriptionStatus.choices, default=SubscriptionStatus.ACTIVE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.nom} - {self.type}"

    class Meta:
        app_label = 'abonnements'
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"
        ordering = ['-date_creation']
        #ordering = ['-date_debut']

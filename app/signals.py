# app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Badge, UserBadge
# Fonction de signal pour déclencher des actions lorsque Model3d est sauvegardé
@receiver(post_save, sender=UserBadge)
def check_for_badges(sender, instance, created, **kwargs):
    # Implémentez la logique pour décerner les badges aux utilisateurs ici
    pass

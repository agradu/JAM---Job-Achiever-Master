from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Application  # Importați modelul Status din models.py

@receiver(pre_save, sender=Application)
def update_status_date(sender, instance, **kwargs):
    if instance._state.adding or instance.status != Application.objects.get(pk=instance.pk).status:
        instance.status_date = timezone.now()
from django.db import models

# Create your models here.
class KariyerAçıklama(models.Model):
    tanim = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Açıklama"